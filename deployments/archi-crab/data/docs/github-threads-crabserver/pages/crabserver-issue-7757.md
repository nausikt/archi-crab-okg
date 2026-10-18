# dmwm/CRABServer issue #7757: Document "high level view" of how CRAB works

State: open
Opened: 2023-07-13T13:48:31Z
Labels: Type: Documentation, Priority: High
URL: https://github.com/dmwm/CRABServer/issues/7757

## Opening post (belforte, 2023-07-13T13:48:31Z)

goal
- what it takes form user env
- what from user directories
- what puts on grid WN, how/where are sandbox extracted
- what's the job wrapper flow
- what does PostJob do
- how to find log files
- pointers to details in twiki

## Comment (belforte, 2023-07-13T13:52:48Z)

@novicecpp @mapellidario @KatyEllis   I think will write the equivalent of a couple pages on the above. From you I'd like to have
1) [twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCrab) or [Wiki](https://github.com/dmwm/CRABServer/wiki) or [MD](https://cmscrab.docs.cern.ch/index.html) ? and feel free to even indicate specific place inside those places
2) comments/additions on the above list

Thanks

## Comment (KatyEllis, 2023-07-13T14:59:13Z)

Hi Stefano,

If this information is at all useful for users then I'd suggest the Twiki. Are the other suggestions internal to CRAB team?

Katy

## Comment (belforte, 2023-07-13T15:35:42Z)

Hi Katy, that's part of the question indeed, do we want to start moving all documentation to MD ? ANd possibly only keep links in twiki ? Or we keep separation ? Clearly things like this are useful to everybody, even to me !

## Comment (novicecpp, 2023-07-13T16:49:13Z)

The bottom line should be: if for the users, use Twiki; otherwise, Markdown.
For existing Twiki and GH wiki pages, use the same rule; if for the users (JobExitCode/CRAB3Configuartion/CRAB3FAQ), do nothing, else migrate to Markdown.

I think "high level view" you list above should be in Markdown because those topics are for operators, but it would be great to put the link in CRAB3FAQ or some Twiki pages, especially the first 2 bullets.
