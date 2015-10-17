import sys
import git

from itertools import chain, imap
from os import path

import matplotlib.pyplot as plt

repo_dir = sys.argv[1]
repo_path = path.realpath(repo_dir)

repo = git.Repo(repo_path)

x_axis, y_axis = [], []

for commit in repo.iter_commits(rev='master'):
    change_size = sum(
        [
             commit.stats.total['insertions'],
             commit.stats.total['deletions'],
        ]
    )

    log_size = sum(
        imap(len, chain(*commit.message.split()))
    )

    if change_size and log_size:
        x_axis.append(change_size)
        y_axis.append(log_size)

figure, axis = plt.subplots()

axis.set_xscale('log')
axis.set_yscale('log')
axis.set_xlabel('Size of the change in a commit')
axis.set_ylabel('Size of the log message in a commit')
axis.scatter(x_axis, y_axis)

figure.savefig('result.png', dpi=figure.dpi)
