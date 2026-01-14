# Simple DCP Python Job
Template job demonstrating basic options; serves as a tutorial and is extensible. See full featured template job here: https://github.com/dan-distributive/dcp-template

* Main job script (`simple-job.py`)
* Browser or Standalone [DCP Workers](https://distributive.network/)

This example shows the full end-to-end workflow with basic options shown for an event-driven distributed job. Input data flows from the client to workers through the scheduler, and results flow back through the scheduler to the client. For direct worker data access that bypasses the scheduler, see remote jobs: https://github.com/dan-distributive/dcp-remote

## Overview

This repository is a tutorial, not a production system. The code emphasizes clarity and is meant to be modified. Configuration and events can be adapted or promoted to command-line prompts for advanced or secure use cases.
If you encounter any issues or have questions, you can reach the team via:

* Email: info@distributive.network
* Slack: [DCP Developers Slack](https://join.slack.com/t/dcp-devs/shared_invite/zt-56v87qj7-fkqZOXFUls8rNzO4mxHaIA)

## Requirements

* Node.js
* Python
* pip packages:
  * dcp
* DCP keystore files in the home directory:
```
~/.dcp/id.keystore
~/.dcp/default.keystore
```
To obtain keystore files, contact: dan@dcp.dev

## Running the Example

**1. Launch the job:**
```
python3 simple-job.py
```

**2. Launch workers**

Here are 3 of the many different types of workers that can be launched:

**Browser worker**

Documentation: [distributive.network/docs/worker-browser.pdf](https://distributive.network/docs/worker-browser.pdf)

Open the following URL, replacing `key` with your compute group join key:
```
https://dcp.work/key
```
Enter the join secret when prompted.

Press `Start`

**Docker Worker**

Documentation: [distributive.network/docs/worker-docker.pdf](https://distributive.network/docs/worker-docker.pdf)

Launch the worker with your account and compute group credentials:
```
docker run -it \
  --earnings-account=<account> \
  --no-global \
  --join <key>,<secret> \
```
* Replace `<account>` with your DCP earnings account number.
* Replace `<key>,<secret>` with your compute group join key and join secret.

**Linux Worker**

Documentation: [distributive.network/docs/worker-linux.pdf](https://distributive.network/docs/worker-linux.pdf)

If the worker is already installed, launch it with:
```
sudo --user=dcp /opt/dcp/bin/dcp-worker.sh \
  --earnings-account=<account> \
  --no-global \
  --join <key>,<secret> \
```
The same credential requirements apply as with the Docker worker.

## Extending the Example

See full featured template job here: https://github.com/dan-distributive/dcp-template

The pattern remains:

```
job = compute_for(input_set, work_function, arguments)
job.exec()
results = job.wait()
```

*Happy computing*
