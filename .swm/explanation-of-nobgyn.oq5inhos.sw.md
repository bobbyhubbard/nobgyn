---
id: oq5inhos
title: Explanation of NOBGYN
file_version: 1.1.2
app_version: 1.9.7
---

# NOBGYN stands for Northland Obstetrics and Gynecology.

## Overview

This document explains the purpose of the NOBGYN repository. Its a simple project which includes fairly straight forward code.

## Language(s)

The primary language of this repo is python utilizing the Django framework for the web and api runtimes.

## Hosting

NOBGYN is hosted via Amazon Web Services LightSail and is currently configured with a single server instance with nightly backups.

## Why Django

Django was selected primarily because I wanted to learn Python at the time and Django was a good option for templatizing a static website for consistency and simple data entry.

It also allowed the client the ability to go into an admin console and update certain content sets themselves.

## Setup

<br/>

Be sure to update the following credentials at deployment time.
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 initial_setup.sh
```shell
20     PASS=$(ssh bitnami@${IPADDR} "cat ~/bitnami_application_password")
21     DJANGO_PROD="%2t!z5vw11(t@fxbln&zvmfvv*pptk*p2mv5^*va&%k9n&we8"
```

<br/>

This file was generated by Swimm. [Click here to view it in the app](https://swimm-web-app--pr-usertest-3105-tg5nt9yp.web.app/repos/Z2l0aHViJTNBJTNBbm9iZ3luJTNBJTNBYm9iYnlodWJiYXJk/docs/oq5inhos).
