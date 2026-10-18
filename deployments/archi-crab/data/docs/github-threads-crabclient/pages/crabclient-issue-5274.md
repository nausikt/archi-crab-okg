# dmwm/CRABClient issue #5274: Print all Publish Containers in crab status command

State: open
Opened: 2023-12-14T17:02:55Z
URL: https://github.com/dmwm/CRABClient/issues/5274

## Opening post (novicecpp, 2023-12-14T17:02:55Z)

`crab status` command in latest version only print Publish Container that have the same name as `tm_output_dataset`. 

![Screenshot from 2023-12-14 17-26-33](https://github.com/dmwm/CRABClient/assets/2346664/173e39f8-f31d-4c88-a3db-2458cc38ff7c)

Now that we have multiple Publish Containers, we need to display all of them.
The info to display is already there in taskdb `tm_multipub_rule`.

## Comment (novicecpp, 2023-12-14T17:06:50Z)

My proposal is print them when supply the `--long` arg.

The new version of `crab status` **without** `--long` (notice the `Publish container's rule` is gone): 
![Screenshot from 2023-12-14 17-24-08](https://github.com/dmwm/CRABClient/assets/2346664/0c26445d-753c-442f-9d89-499861d5f94e)

**with** `--long`, it will print Publish Container's name and its rule after Publication section:
![Screenshot from 2023-12-14 17-23-47](https://github.com/dmwm/CRABClient/assets/2346664/7be70b72-3372-42dc-942c-2b02554cd8f6)

@belforte What do you think?

## Comment (belforte, 2023-12-14T17:31:02Z)

I'd rather add a new option than expect/ask users to use --long with task of >100 jobs.
But.. are we talking about one line for each output file ? I.e. mostly one at at most a handful ? Why not adding them all of the times ?
I agree that the crab status output is getting long. But suggest to keep looking for ideas.
Maybe add an option to list rules ? In the end rules on Publish container are not very useful, esp. if they have no expiration date. And one can simply to `rucio rule-info <container>`. Maybe one line about this ?

Anyhow, I would really really stay out of `status --long`

## Comment (novicecpp, 2023-12-15T04:40:38Z)

> Maybe add an option to list rules ? In the end rules on Publish container are not very useful, esp. if they have no expiration date. And one can simply to rucio rule-info <container>. Maybe one line about this ?

I don't think so.
I *always* use the rule ID as the starting point when interact with the Rucio system, mainly because it has GUI that easy to navigate around. If it not enough, then I will go to the CLI like `list-file-replicas` or `list-account-usage` command.
It also tell the users which rule is created and managed by CRAB.

. 

About the `--long` I kinda agree with you. I personally do not mind having the longer output, and as the reason above, I still want to show both the container name and rule ID. 

Maybe a new arg like `--show-containers` is the best option where we can keep status output short, trade-off with a little extra effort required from users to provide additional arg. We can also add more information to the output like rule expiration time or lock status summary.
