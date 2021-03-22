# UAB Website

#### Getting Started

This repo contains all code required to run our website, it is a [svelte](https://svelte.dev/) app using a custom [tornado](https://www.tornadoweb.org/en/stable/) package to serve the site.

See below for basic instructions for connecting to the server hosting the website, using TMUX, and how to run and make changes to the website.

### Connecting

Our website's server runs on a linux server hosted by the [Cybera Rapid Access Cloud (RAC)](https://rac-portal.cybera.ca/users/sign_in). Speak with the software team lead or club president to get SSH access for the admin account.

### Serving the website

Attach to the "Webserver" TMUX session (see below for details and commands), cd to the uab\v2-website directory, and run `sudo ./run.sh`.

### TMUX

##### Overview

[TMUX](https://github.com/tmux/tmux/wiki) is short for Terminal Multiplexer. Essentially, it is a way to have multiple terminal sessions active at once from a command line interaface.

This allows us to have 2 sessions, with different purposes. Our 3 sessions are as follows:
  1. **Webserver**: Runs the main webserver app, if this isn't running you won't be able to browse to the website.
  2. **Applications**: Handles new applications

##### Commands

A very basic guide to get started with TMUX can be found [here](https://linuxize.com/post/getting-started-with-tmux/) and a more detailed guide [here](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/).

The prefix for all tmux commands is `CTRL + B` this can be changed via the tmux.conf file. Some basic commands to get you started are below.

**List all sessions**

`tmux ls`

**Attach to a session**

`tmux attach-session -t <session name>` or `tmux a -t <session name>`

**Detach from current session**

`CTRL + b` `d`

**Create a new session**

`tmux new -s <session name>`

**End a session**

`tmux kill-session -t <session name>`


#### Dependecies
python3 -m pip install tornado pysha3 pymysql