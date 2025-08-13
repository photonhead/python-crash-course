# first_name = "steve "
# last_name = " jobs"
# quote = "You can't connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future."
# message = f'{first_name.strip().title()} {last_name.strip().title()} once said, "{quote}"'
# print(message)

famous_person = " steve jobs "
quote = "You can't connect the dots looking forward; you can only connect them looking backwards. So you have to trust that the dots will somehow connect in your future."
link = 'https://news.stanford.edu/stories/2005/06/steve-jobs-2005-graduates-stay-hungry-stay-foolish'
filename = 'python_note.txt'

message = f'\t{famous_person.strip().title()} once said, "{quote}"\n\tHis Stanford commencement speech in 2005 was resonated with me, and that quote became a motto of my life.\n\tYou can watch his full speech here: {link.removeprefix('https://')}\n\tYou also can find the link in this file: {filename.removesuffix('.txt')}\n\tThank you!'
print(message)