# Forks: A story

A collaborative narrative told through automation.

Nov 19, 2022: This is a work in progress. Please do not fork the repository at this time.

The conceit is that a journey of some kind is started by the user at the root of the repository tree, [forks-a-story/forks](https://github.com/forks-a-story/forks). Any immediate children of that repository have joined the journey early, and know who started it.

The story is automatically published on the Github Pages site for any repository, e.g. https://forks-a-story.github.io/forks/ for the root story.

## Joining the story

All that is required is to [fork this repository](https://github.com/forks-a-story/forks/fork) and you will be
added to the story upstream.

You are encouraged to fork [other forks](https://github.com/lizadaly/forks/network/members) of this repository rather
than forking from the root. Doing so will generate a more interesting story!
Here are the current [list of forks](https://github.com/lizadaly/forks/network/members).
If a fork's code has deviated from the original repository, make sure you're comfortable with its changes.

You are encouraged to also generate a version of the story from your point of view. Doing so only requires
modifying some settings in your fork of this repository.

* **Read the "Privacy, safety, and security" section below.**
* Go to the Actions tab in your fork, and enable Workflows.
* Now go to Settings in your fork.
* Select "Pages" from the left nav.
* Under "Build and deployment", select "Github Actions."

The story will automatically be built at `https://<your-username>.github.io/forks/`.

A fork can see limited activity "above it", and any activity "below it"—any forks of your fork.

## Privacy, safety, and security

Simply forking this repository will add your username to the story. Deleting your fork will
remove you from the story, though not everyone's fork will immediately reflect that change.

Choosing to enable the Github Actions workflow will cause your version of the story to be automatically
published whenever you update the code, or whenever anyone forks your fork. Because the
repository is public, as of November 18, 2022 [according to the Github documentation](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions),
running the workflow should not incur any cost. This could change in the future!

The workflow will use the default [GITHUB_TOKEN](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)
to run the action. Its permissions are restricted to the repository and
public information. To be as considerate as possible of unintended data sharing, no other user information
besides the username of the repository is included in the story. However, other user data,
like public URLs or Twitter handles, are potentially available to the token.
### Modifying the output

Any user modifying the output of the story in their fork must abide by the
[Code of Conduct](https://github.com/forks-a-story/forks/blob/main/CODE_OF_CONDUCT.md).
You may also submit a pull request to the root repository to have
your changes incorporated there.

Be aware that if you are forking a fork, there may be changes to the Github Action or its output
that aren't in the root. It's possible these changes could produce harmful output.
If you see such a misuse, please report the [abuse to Github](https://docs.github.com/en/communities/maintaining-your-safety-on-github/reporting-abuse-or-spam)
and [notify me](lizadaly@gmail.com) privately so I can block the user.

