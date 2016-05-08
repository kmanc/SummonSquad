# Riot_Challenge_2016

This project's goal is to find you and 4 friends your "optimum" team based on champion mastery.  It currently takes each summoners top 10 champions by mastery score (that number may be customizable in the future), and tests each possible team combination for those champs (That's 100,000 possible teams!).  We first filter out any team that doesn't have one champion in each of the 5 standard positions, because we don't want to suggest that you play with 4 mid laners and a jungler.  Based on a scoring algorithm we developed, it assigns each of those teams a score, and at the end, we give you the team that scored highest on our index!

In the future we want to do a few things to make our tool more realistic.  For instance, we want to be able to adjust teams based on the champions we suggest as some of them are banned or picked in the draft.  We also want to add modifiers to increase the liklihood of suggesting champions that are considered strong in the current meta, so you can rest assured your team gives you the best chance to win.

There are a few issues that we are working through, and hope to have solved soon(ish):
    Right now we only support NA
    You have to have played ranked in order for us to know what role you play a champion in (because the api does not give us             role information for normal games)
    We made this in 10 days, so bugs pop up now and then.  We could actually really sue your help...if you see one, let us               know so we can squash it!!
