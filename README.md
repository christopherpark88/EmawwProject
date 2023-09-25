# emaww-th

Prerequisites: Need Docker

Includes a sample xml, config.xml in root.

Sample input to run from project root directory:

`./export.sh -v ./config.xml`

Can handle any input of format:

`export.sh -v /path/to/xml`

# Warnings

- Path is relative to project root directory.
- Furthermore, typically will require running "./export.sh" instead of "export.sh" (see above two examples), because unlikely "./export.sh" wil be in $PATH (nothing can be done about this from my side, has to be on your local).
