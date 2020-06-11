# Automate Project Initialization

Automate the initialization of projects. Projects are created with, a README.md
that can include a project description, a .gitignore and are created
locally either with or without a remote to github.

---

```create \<project name>```
* Initiates a remote git project in projects/myProjects called \<project name>
with github remote repo under the same name.
* ```-R -r``` specifies initiating a remote repo
* ```-L -l``` specifies initiating a local repo
* ```-P -p``` specifies the creation of a private repo --Note: a private repo
is only possible with a remote initiation.
* ```-D <description> -d <description>``` specifies the description to add to
the repo and README
* ```-DO <description> -do <description>``` specifies the description to add 
to the repo only
* ```-e <editor>``` specifies the editor to open the project in

---
#### .gitignore compatibility
* Clion
* Intellij
* PyCharm
* Visual Studio Code
* Eclipse
