from github import Github
import time

# Authentication for the user into github.com

g = Github("Testask", "Testask84218421")
u = g.get_user()


# Deleting of all existing repositories on github.com

def check_rep():
    for repo in u.get_repos():
        repo.delete()

    repo_count = len([i for i in u.get_repos()])
    while repo_count != 0:
        repo_count = len([i for i in u.get_repos()])

    # Create a repository on github.com
    u.create_repo("Elmira")
    time.sleep(30)


def repos_sum():
    repos = u.get_repos()

    # test 1
    assert len([i.name for i in repos]) == 1, "Should be 1 repository"


# Create an issue on github.com

def create_issue():
    repo = g.get_repo('Testask/Elmira')
    issue = repo.create_issue(title="This is a new issue")
    founded_issue = repo.get_issue(number=issue._number.value)

    # test 2
    assert issue == founded_issue, "The test with issue creating was not passed"


# Create a Milestone on github.com

def create_milestone():
    repo = g.get_repo('Testask/Elmira')
    milestone = repo.create_milestone(title='New Milestone')
    created_milestone = repo.get_milestone(number=1)

    # test3
    assert milestone == created_milestone, "The test with milestone creating was not passed"


# Create a new file in the repository

def create_new_file():
    repo = g.get_repo('Testask/Elmira')
    repo.create_file("test.txt", "test", "test", branch="test")
    time.sleep(5)
    contents = repo.get_contents("")

    # Get list of files
    l = list()
    for content_file in contents:
        l.append(content_file.name)

    # test4
    assert l[0] == 'test.txt', "There is an error with list of files"


# Get all the labels of the repository

def get_all_labels_repository():
    repo = g.get_repo('Testask/Elmira')
    labels = repo.get_labels()
    l = list()
    for label in labels:
        l.append(label.name)

    # test5
    assert 'bug' in l, "There is no such label"


if __name__ == "__main__":
    check_rep()
    repos_sum()
    create_issue()
    create_milestone()
    create_new_file()
    get_all_labels_repository()

    print("Everything is passed succesfully")
