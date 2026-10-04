# syntax=docker/dockerfile:1.7
# archi v2 images for the benchmark, built from archi `main` at a PINNED commit (v2/versions.lock).
#
#   target data-manager  ghcr.io/nausikt/archi-v2-data-manager   archi's headless ingestion service
#   target mcp           ghcr.io/nausikt/archi-v2-mcp            the same image + v2/mcp/server.py
#
# The data-manager stage is upstream's Dockerfile-data-manager-universal (vendored next to
# this file under v2/vendor/reference/dockerfiles/, so an upstream change shows as a diff on
# the engine PR) with ONE difference: the source comes from git at ARCHI_COMMIT instead of a
# checked-out tree, so the image is a pure function of (BASE_IMAGE, ARCHI_COMMIT).
#
#   docker build -f v2/docker/Dockerfile --target mcp \
#     --build-arg BASE_IMAGE=$(v2/scripts/lock.sh base-ref) \
#     --build-arg ARCHI_COMMIT=$(yq -r .archi.commit v2/versions.lock) .
#
# Build context: the repository root (COPY v2/mcp). No secrets are needed: archi is public.
ARG BASE_IMAGE=ghcr.io/nausikt/archi-v2-python-base:latest   # OURS (v2/docker/Dockerfile.base), pinned by digest in the lock
ARG ARCHI_REPO=https://github.com/archi-physics/archi.git
ARG ARCHI_COMMIT=main
# The HuggingFace embedding model is baked in (HF_HOME inside the image), so neither the
# data-manager nor the vector MCP downloads anything at start: deterministic, and no egress.
# Must match data_manager.embedding_class_map.HuggingFaceEmbeddings.kwargs.model_name
# (v2/deployments/archi-crab/config.yaml); empty = bake nothing (OpenAI embeddings).
ARG HF_PREFETCH_MODEL=sentence-transformers/all-MiniLM-L6-v2

# ---------------------------------------------------------------- data-manager ----
FROM ${BASE_IMAGE} AS data-manager
ARG ARCHI_REPO
ARG ARCHI_COMMIT
RUN mkdir -p /root/archi
WORKDIR /root/archi

# Install Firefox and Geckodriver for Selenium (upstream keeps them in the data-manager image;
# only the SSO/selenium scrapers use them, which this deployment has off)
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    gnupg \
    git \
    ca-certificates \
    --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Geckodriver (architecture-aware)
ARG TARGETARCH
RUN GECKO_VERSION="v0.36.0" && \
    if [ "$TARGETARCH" = "arm64" ]; then \
        GECKO_ARCH="linux-aarch64"; \
    else \
        GECKO_ARCH="linux64"; \
    fi && \
    wget -q "https://github.com/mozilla/geckodriver/releases/download/${GECKO_VERSION}/geckodriver-${GECKO_VERSION}-${GECKO_ARCH}.tar.gz" \
    && tar -xzf "geckodriver-${GECKO_VERSION}-${GECKO_ARCH}.tar.gz" -C /usr/local/bin \
    && chmod +x /usr/local/bin/geckodriver \
    && rm "geckodriver-${GECKO_VERSION}-${GECKO_ARCH}.tar.gz"

# archi at the pinned commit (BuildKit git source; no .git dir is kept in the image)
ADD ${ARCHI_REPO}#${ARCHI_COMMIT} /tmp/archi
RUN cp -r /tmp/archi/src src \
    && cp /tmp/archi/pyproject.toml /tmp/archi/LICENSE . \
    && rm -rf /tmp/archi \
    && pip install --upgrade pip && pip install .

RUN chmod g+rx /root; chmod -R g+w /root/archi/src/interfaces

ARG HF_PREFETCH_MODEL
ENV HF_HOME=/opt/hf
RUN if [ -n "$HF_PREFETCH_MODEL" ]; then \
      python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('$HF_PREFETCH_MODEL')" \
      && chmod -R a+rX /opt/hf; \
    fi

# The two are read by v2/mcp/server.py (server version) and the contract check
ENV ARCHI_COMMIT=${ARCHI_COMMIT} ARCHI_ROOT=/root/archi
LABEL org.opencontainers.image.source="https://github.com/nausikt/archi-crab-okg" \
      org.opencontainers.image.revision="${ARCHI_COMMIT}" \
      org.opencontainers.image.title="archi-v2-data-manager"

CMD ["python", "-u", "src/bin/service_data_manager.py"]

# ----------------------------------------------------------------------- mcp ----
FROM data-manager AS mcp
COPY v2/mcp /root/archi/v2mcp
COPY v2/scripts/contract-check.py v2/scripts/smoke.py /root/archi/v2mcp/
RUN pip install --no-cache-dir -r /root/archi/v2mcp/requirements.txt
ENV V2_MCP_FAMILY=grep V2_MCP_PORT=8081
EXPOSE 8081
LABEL org.opencontainers.image.title="archi-v2-mcp"
CMD ["python", "-u", "/root/archi/v2mcp/server.py"]
