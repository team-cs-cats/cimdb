# 2Fast4U Computer Inventory Management Database (CIMDB)
Web-based CRUD database. 


<!-- ABOUT THE PROJECT -->
## About The Project

2Fast4U Computers assembles and sells $2 million in PCs annually (on average 1,500 PCs assembled per year). The Computer Inventory and Manufacturing (CIM) web app will help manage the inventory, assembly, and quality control (QC) process for 2Fast4U. The state of the art database (DB) behind the CIM webapp will be used by 2Fast4U Employees at different production Sites. Employees are assigned Work Orders, which list Products to assemble using Regular Components (which are available in large quantities like MotherBoard, RAM, etc.) and Special Components (CPUs, which must be tracked using unique serial numbers). Regular Components and Special Components are stored in Locations at any particular Site until they are used to assemble Products. Once each Product has been assembled and QC’d, the Work Order can be closed.

This class project was built for Oregon State's CS340 Databases class in Winter 2021.

The project is hosted live on Heroku at https://team-cs-cats.herokuapp.com/

**Note: When loading the hosted website, please be patient as it takes several seconds for the Heroku server to spin up and load the site files.**


<!-- ### Built With -->
### Built With
* [Flask](https://flask.palletsprojects.com/en/1.1.x/): a Python framework for developing web applications. 



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In order to make local changes to the CIMDB, you must first have Python and pip installed on your system. If you need assistance installing these prerequisites, see the folowing steps:
* Python is a programming language. Almost all of this project's code base (particularly the backend) is written in Python. Download the latest version of [Python](https://www.python.org/downloads/) and install onto your local machine.

* Pip is the package installer for Python. Once Python is installed, open your local machine's command line and use the following command to utilize Python to install Pip:
```sh
python get-pip.py -g
```

Git is a version control system. In this project, Git is used to clone (copy) the most up-to-date project files from GitHub to your local machine. Download the latest version of [git](https://git-scm.com/download/win) and install on your local machine.


### Installation (will change based on project setup) 

1. Open the command line on your local machine.

2. Enter the following command to use Git to clone this repository to your local machine.
```sh
git clone https://https://github.com/team-cs-cats.git
```
3. Create a virtual environment called `env` within your local cloned repository.
```sh
virtualenv env
```
4. Activate the `env` virtual environment.
```sh
env\Scripts\activate.bat
```
5. Enter the following command to use Pip to install this repository's dependencies.
```sh
pip install -r requirements.txt
```
6. To run a local copy of the website on your local execute the `run.py` file.
```sh
python run.py
```
7. On your browser, navigate to `http://localhost:5000/`. This will update to saved changes in your local directory upon refresh.
8. Occasionally, some of the built-in resources (particularly the javascript scripts) of this project do not update when reloading changes made to files. To bypass these errors, reload the web page and bypass the cache. This can be done using the `Shift + left click Reload button` on Firefox or by entering developer mode on Google Chrome and selecting the `Empty Cache and Hard Reload` option.

<!-- USAGE EXAMPLES -->
## Usage



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/team-cs-cats/cimdb/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE](https://github.com/team-cs-cats/cimdb/LICENSE.txt) for more information.



<!-- CONTACT -->
## Contact

Ali Jalilian - jalilian@oregonstate.edu
Asa LeHolland - hollaasa@oregonstate.edu

Project Link: [https://github.com/team-cs-cats/cimdb](https://github.com/team-cs-cats/cimdb)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew](https://github.com/othneildrew) for creating the [template README file](https://github.com/othneildrew/Best-README-Template) that was used as the starting point for the README for this project. 





<!-- MARKDOWN LINKS & IMAGES (to be added as needed) -->
<!-- [example-use]: images/{filename}.gif -->

