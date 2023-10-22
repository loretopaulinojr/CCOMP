# GitHub Tutorial: Agile & Continuous Testing

- **Who is this for**: Anyone interested in starting using GitHub for Continuous testing/integration.
- **What you'll learn**: We'll introduce repositories, issues, kanban boards, branches, commits, pull requests, tests, and workflows.
- **What you'll build**: We'll write some short code (a Hello World function) and a automated test for it.
- **Prerequisites**: None. This course is a great introduction for your first day on GitHub.
- **How long**: This course is four steps long and takes less than one hour to complete.

_Welcome to "Introduction to GitHub"! :wave:_

**What is GitHub?**: GitHub is a collaboration platform that uses [Git](https://docs.github.com/get-started/quickstart/github-glossary#git) for versioning. GitHub is a popular place to share and contribute to [open-source](https://docs.github.com/get-started/quickstart/github-glossary#open-source) software.
<br>:tv: [Video: What is GitHub?](https://www.youtube.com/watch?v=w3jLJU7DT5E)

**What is Sourcetree**: [Sourcetree](https://www.sourcetreeapp.com/) is a free Git client for Windows and Mac. It is useful both for beginers or people with little command line experience, AND for experts who want to do more advanced work like reviewing changesets, stashing, cherry-pick ingbetween branches and more.

## How to use this tutorial

1. Above these instructions, right-click **Use this template** and open the link in a new tab.
   ![Use this template](https://user-images.githubusercontent.com/1221423/169618716-fb17528d-f332-4fc5-a11a-eaa23562665e.png)
2. In the new tab, follow the prompts to create a new repository.
   - For owner, choose your personal account or an organization to host the repository.
   - We recommend creating a public repository—private repositories will [use Actions minutes](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions).
   ![Create a new repository](https://user-images.githubusercontent.com/1221423/169618722-406dc508-add4-4074-83f0-c7a7ad87f6f3.png)
3. After your new repository is created, wait about 20 seconds, then refresh the page. Follow the step-by-step instructions in the new repository's README.

<details id=1>
<summary><h2>Step 1: Open an Issue and Track on a Kanban board</h2></summary>

**Issues** let you track your work on GitHub, and are useful for discussing specific details of a project such as bug reports, planned improvements and feedback.

Let's open some issues about the work we are going to do today.

1. On GitHub.com, navigate to the main page of the repository.
2. Under your repository name, click Issues.
3. Click New issue.
4. Type a title and description for your issue. We will title our first issue "Write function that says hello to a given name".
5. When you're finished, click Submit new issue.

Repeat that process to create the following issues:
* Test the hello function
* Automatically build and test code

Another way to track your issues is by using **Projects**. A project is an adaptable spreadsheet that integrates with your issues and pull requests on GitHub to help you plan and track your work effectively. 

We'll make a project for our work:

1. In the top right corner of GitHub.com, click your profile photo, then click Your profile.
2. On your profile, click  Projects.
3. Click New project.
4. When prompted to select a template, click a template or, to start with an empty project, click Board. Then, click Create.

The board view of the project is essentially a **Kanban board**.

A kanban board is an agile project management tool designed to help visualize work, limit work-in-progress, and maximize efficiency (or flow).

We can add the issues we have already created to the board by clicking the "Add Item" button at the bottom of the Todo column and searching for your repository using the `#` key.

</details>

<details id=2>
<summary><h2>Step 2: Clone your Repository Using SourceTree</h2></summary>
**What is a repository?**: A [repository](https://docs.github.com/get-started/quickstart/github-glossary#repository) is a project containing files and folders. A repository tracks versions of files and folders.
<br>:tv: [Video: Exploring a repository](https://www.youtube.com/watch?v=R8OAwrcMlRw)

1. From SourceTree, click Remote. All of your remote projects display.
<img alt="image showing my-first-branch entry" src="sourcetree_home_screenshot.png"/>
2. Click Clone next to the repository you wish to clone locally.
3. From the Clone a repository window, click Clone. Click Local to see a list of your cloned repositories. 
</details>

<details id=3>
<summary><h2>Step 3: Create branches for Trunk Based Development</h2></summary>

### :keyboard: Activity: Your first branch with Sourcetree

**What is a branch?**: A [branch](https://docs.github.com/en/get-started/quickstart/github-glossary#branch) is a parallel version of your repository. By default, your repository has one branch named `main` and it is considered to be the definitive branch. You can create additional branches off of `main` in your repository. You can use branches to have different versions of a project at one time.

On additional branches, you can make edits without impacting the `main` version. Branches allow you to separate your work from the `main` branch. In other words, everyone's work is safe while you contribute.
<br>:tv: [Video: Branches](https://www.youtube.com/watch?v=xgQmu81G1yY)

**What is Trunk-Based Development?** [Trunk Based Development]() is a branching model, where developers collaborate on code in a single branch called ‘trunk’ (or on their short lived feature branches). You should resist any pressure to create other long-lived development branches by employing documented techniques. You avoid merge hell, do not break the build, and live happily ever after. ![Trunk Based Dev Diagram](https://trunkbaseddevelopment.com/trunk1c.png)

Instead of a single main branch, we will use two branches to record the history of the project. The main branch stores the official release history, and the develop branch serves as an integration branch for features. It's also convenient to tag all commits in the main branch with a version number.

The first step is to complement the default main with a develop branch. A simple way to do this to create empty develop branch locally and push it to the server.

1. From Sourcetree, click the Branch button.
2. From the New Branch field, enter a name for your branch- we'll call this one "develop".
3. Click Create Branch.

_You created a branch! :tada:_

Now, do the same for a feature branch, we'll call "hello".

Now you are all set to start developing!

</details>

<details id=4>
<summary><h2>Step 4: Commit a file</h2></summary>

Now that you are on your feature branch, you can edit your project without changing the `main` branch. It’s time to create a file and make your first commit!

**What is a commit?**: A [commit](https://docs.github.com/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits) is a set of changes to the files and folders in your project. A commit exists in a branch.

### :keyboard: Activity: Your first commit

The following steps will guide you through the process of committing a change on GitHub using Sourcetree. Committing a change requires first adding a new file to your new branch. 

1. In your favorite IDE, make sure you're on your new branch `hello`.
2. Open the file called `hello.py` in the directory `hello`.
3. In your IDE, copy the following content to your file:
   ```
   def hello(name: str):
        print('Hello, ' + name + '!')
   ```
4. Open the History view in SourceTree and notice that your repository now has uncommitted changes.
5. Click the check mark next to `Unstaged Files` to stage all of your changes.
6. In the message box, enter a commit message.
7. Click the Commit button under the box. From Sourcetree's History, you'll see that the file has been updated on your new branch.
8. Click the Push button to push your new branch to the repository.
9. Under the Push? column from the dialog box that appears, select your new branch to indicate that you are pushing that branch to origin and click OK.
</details>

<details id=5>
<summary><h2>Step 5: Create a test</h2></summary>

**What is unittest?**: The unittest module provides a rich set of tools for constructing and running tests. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

In the `test` directory, there is a file called `test_hello.py` to test `hello.py`- we will add 2 tests to the file.

1. Create a test that passes your name to the function and checks that the output is as expected.
2. Create a test that passes an integer, and check the the function fails.
3. You can set up to run these tests more interactively.

</details>

<details id=6>
<summary><h2>Step 6: Open a pull request</h2></summary>

_Nice work making those commits :sparkles:_

Now that you’ve created a commit, it’s time to share your proposed change through a pull request!

**What is a pull request?**: Collaboration happens on a pull request. The pull request shows the changes in your branch to other people. This pull request is going to keep the changes you just made on your branch and propose applying them to the `develop` branch.
<br>:tv: [Video: Introduction to pull requests](https://youtu.be/kJr-PIfLDl4)

### :keyboard: Activity: Create a pull request

You may have noticed after your commit that a message displayed indicating your recent push to your branch and providing a button that says **Compare & pull request**.

![screenshot of message and button](/images/compare-and-pull-request.png)

 If you want, feel free to click **Compare & pull request**, and then skip to step 6 below. If you don't click the button, the instructions below walk you through manually setting up the pull request.

1. Click on the **Pull requests** tab in your repository.
2. Click **New pull request**.
3. In the **base:** dropdown, make sure **main** is selected.
4. Select the **compare:** dropdown, and click `my-first-branch`. <br>
   <img alt="screenshot showing both branch selections" src="/images/pull-request-branches.png"/>
5. Click **Create pull request**.
6. Enter a title for your pull request: `Add my first file`.
7. The next field helps you provide a description of the changes you made. Feel free to add a description of what you’ve accomplished so far. As a reminder, you have: created a branch, created a file and made a commit! <br>
   <img alt="screenshot showing pull request" src="/images/Pull-request-description.png"/>
8. Click **Create pull request**.
9. Move on to Step 4! <br>
   **Note**: Like before, you can wait about 20 seconds, then refresh this page (the one you're following instructions from) and [GitHub Actions](https://docs.github.com/en/actions) will automatically close this step and open the next one. As a perk, you may see evidence of GitHub Actions running on the tab with the pull request opened! The image below shows a line you might see on your pull request after the Action finishes running.<br>
   <img alt="screenshot of an example of an actions line" src="/images/Actions-to-step-4.png"/>

</details>

<details id=7>
<summary><h2>Step 7: Merge your pull request</h2></summary>

_Nicely done friend! :sunglasses:_

You successfully created a pull request. You can now merge your pull request.

**What is a _merge_**: A [merge](https://docs.github.com/en/get-started/quickstart/github-glossary#merge) adds the changes in your pull request and branch into the `main` branch.
<br>:tv: [Video: Understanding the GitHub flow](https://www.youtube.com/watch?v=PBI2Rz-ZOxU)

As noted in the previous step, you may have seen evidence of an action running which automatically progresses your instructions to the next step. You'll have to wait for it to finish before you can merge your pull request. It will be ready when the merge pull request button is green.

![screenshot of green merge pull request button](/images/Green-merge-pull-request.png)
### :keyboard: Activity: Merge the pull request

1. Click **Merge pull request**.
1. Click **Confirm merge**.
1. Once your branch has been merged, you don't need it anymore. To delete this branch, click **Delete branch**.<br>
   <img alt="screenshot showing delete branch button" src="/images/delete-branch.png"/>
2. Check out the **Finish** step to see what you can learn next!<br>
   **Note**: Like before, you can wait about 20 seconds, then refresh this page (the one you're following instructions from) and [GitHub Actions](https://docs.github.com/en/actions) will automatically close this step and open the next one.

</details>

<details id=8>
<summary><h2>Step 8: Set up an automated workflow</h2></summary>

**GitHub Actions** is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.

You can configure a GitHub Actions *workflow* to be triggered when an *event* occurs in your repository, such as a pull request being opened or an issue being created. Your workflow contains one or more *jobs* which can run in sequential order or in parallel. Each job will run inside its own virtual machine runner, or inside a container, and has one or more steps that either run a script that you define or run an action, which is a reusable extension that can simplify your workflow.

We will create a workflow to run our tests every time you push to a branch, and every time you open a pull request. This will let you know if any changes have broken your code unexpectedly, and if your code is safe to merge into the development branch.

1. Make a new feature branch for setting up the action.
2. In your repository, create the .github/workflows/ directory to store your workflow files.
3. In the .github/workflows/ directory, create a new file called learn-github-actions.yml and add the following lines:
   1. Define the name of the workflow as it will appear in the "Actions" tab of the GitHub repository.
   ```
   name: Python package
   ```
   2. Specify the trigger(s) for the action. This example used the `push` and `pull_request` event, so a workflow run is triggered every time someone pushes a change to the repository (on any branch) or opens a pull a request.
   ```
   on:
   push:
   pull_request:
   ```
   3. Group together all the jobs that run in the workflow.
   ```
   jobs:
   ```
   4. Define a job named `build`.
   ```
      build:
   ```
   5. Define the type of machine to run the job on. Here we will use a GitHub-hosted runner, specifically a virtual machine of the latest version of Ubuntu Linux.
   ```
         runs-on: ubuntu-latest
         strategy:
   ```
   6. You can control how job failures are handled with jobs. If `fail-fast` is set to `true`, GitHub will cancel all in-progress and queued jobs in the matrix if any job in the matrix fails, which is the default. Here we will set it to false so that all jobs run regardless if one fails.
   ```
         fail-fast: false
   ```
   7. We will test our code on multiple python versions, listed here.
   ```
         matrix:
            python-version: ["3.8", "3.9", "3.10"]
   ```
   8. Group together all the steps that run in the `build` job. Each item nested under this section is a separate action or shell script.
   ```
         steps:
   ```
   9. The `uses` keyword specifies that this step will run `v3` of the `actions/checkout` action. This is an action that checks out your repository onto the runner, allowing you to run scripts or other actions against your code (such as build and test tools). You should use the checkout action any time your workflow will run against the repository's code.
   ```
         - uses: actions/checkout@v2
   ```
   10. This step uses the `actions/setup-python@v2` action to install the specified version of python.
   ```
         - name: Set up Python ${{ matrix.python-version }}
           uses: actions/setup-python@v2
           with:
              python-version: ${{ matrix.python-version }}
   ```
   11. The `run` keywork tells the job to execute a command on the runner. In this case you are using python to pip install the tools you need to run the workflow.
   ```
         - name: Install dependencies
         run: |
            python -m pip install --upgrade pip
            python -m pip install flake8 pytest
            if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
   ```
   12. Here, the `run` keyword is using flake8 to lint the code.
   ```
            - name: Lint with flake8
            run: |
               # stop the build if there are Python syntax errors or undefined names
               flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
               # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
               flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
   ```
   13. Here the `run` keyword installs the code we wrote (in the hellofolder) and uses pytest to run the tests in our test folder.
            - name: Test with pytest
            run: |
               pip install .
               pytest
```
4. Commit these changes and push them to your GitHub repository.
5. We can view the activity for a workflow run on the GitHub website.
   1. Under the repository name, click Actions.
   2. Here we have only a single workflow, but if you had multiple, you could click on the name of the workflow you are interested in in the left sidebar to see only those results.
   3. To get more details on a single workflow run, click on the name of the event that triggered the workflow.
   4. From there, you can look at individual jobs, and their console output.

</details>
