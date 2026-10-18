# dmwm/CRABServer issue #8929: add WAITING status to task status diagram

State: closed
Opened: 2025-02-17T14:17:00Z
Closed: 2025-02-25T13:35:57Z
Labels: Type: Documentation
URL: https://github.com/dmwm/CRABServer/issues/8929

## Opening post (belforte, 2025-02-17T14:17:00Z)

update https://cmscrab.docs.cern.ch/crab-design/crab-task-state.html with new status flow after introduction of task scheduling

## Comment (aspiringmind-code, 2025-02-25T11:14:31Z)

Done in [Fix#8929](https://gitlab.cern.ch/crab3/cms-crab-docs/-/commit/ec5f31dbfdd7f4e33d2ad4eb333630d3fd861437)

## Comment (belforte, 2025-02-25T13:15:45Z)

thanks Vijay. Sorry, I should know but.. does Canary really put tasks in NEW ?

side Q: how do you like plantuml ? any thought of moving to mermaid ? https://cmscrab.docs.cern.ch/documentation/plantuml.html

## Comment (aspiringmind-code, 2025-02-25T13:26:59Z)

Oops, sorry. you are right. runCanary doesn't put in NEW. Let me remove runCanary from the diagram. I haven't used either plantUML or mermaid before. I used LucidChart to add the status.

## Comment (aspiringmind-code, 2025-02-25T13:35:57Z)

[Updated](https://gitlab.cern.ch/crab3/cms-crab-docs/-/commit/1d410f86d34b8a3368f28f1c45f379c122d78e94)

## Comment (aspiringmind-code, 2025-02-25T13:42:25Z)

I'll explore plantUML and mermaid and let you know which I like better.
