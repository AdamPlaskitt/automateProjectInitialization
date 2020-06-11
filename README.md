# Automate Project Initialization

Automate the initialization of projects. Projects are created with, a README.md
that can include a project description, a .gitignore and are created
locally either with or without a remote to github.

---

```create \<project name>```
* Initiates a remote git project in projects/myProjects called \<project name>
with github remote repo under the same name.
* ```-R -r``` Specifies initiating a remote repo
* ```-L -l``` Specifies initiating a local repo
* ```-P -p``` Specifies the creation of a private repo --Note: a private repo
is only possible with a remote initiation.
* ```-D <description> -d <description>``` Specifies the description to add to
the repo and README
* ```-DO <description> -do <description>``` Specifies the description to add 
to the repo only
* ```-e <editor>``` Specifies the editor to open the project in
* ```-cd <path>``` Overrides the default path with the provided path

---
#### .gitignore compatibility
* Clion
* Intellij
* PyCharm
* Visual Studio Code
* Eclipse
