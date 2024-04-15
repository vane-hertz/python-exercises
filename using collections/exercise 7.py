info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info_list = info.split(':')
final_info = '+'.join(info_list)
print(final_info)