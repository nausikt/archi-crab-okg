# dmwm/CRABServer issue #9343: deprecate /etc/proxy/proxy, update via ArgoCD + helm, update deployment instructions

State: open
Opened: 2026-07-07T09:37:08Z
Labels: Area: Code Cleanup, Area: zK8s
URL: https://github.com/dmwm/CRABServer/issues/9343

## Opening post (nausikt, 2026-07-07T09:37:08Z)

Stefano found that we can safely deprecate `/etc/proxy/proxy`. (we actually live with expired proxy for all this time)

Also It would be great to clean up X509_USER_PROXY, X509_USER_{CERT|KEY} thus no longer confuse ourself or new operator.
and took this chances to update new ArgoCD + helm deployment instructions.

## Comment (nausikt, 2026-07-27T10:10:49Z)

Again don't forget to update https://cmscrab.docs.cern.ch/crab-components/crab-rest/deploy.html from "Helm" to "argoCD"
