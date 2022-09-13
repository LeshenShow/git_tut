name = 'gus'
print(name)

# cmd \\ terminal write:
# cd Name \\ or cd "C:\My projects\plots\animation"  - заходим в данную папку
# dir - что есть в папке
# git clone https://github.com/LeshenShow/git_tut.git -клонируем репозиторий в папку

# Потом заходим в папку с проекторм cd C:\My projects\Туториалы\Git_tuts\git_test\git_tut
# Добавляем новый наш файл в репозиторий (step 1) C:\My projects\Туториалы\Git_tuts\git_test\git_tut>git add hello.py
# Делаем commit (step 2): C:\My projects\Туториалы\Git_tuts\git_test\git_tut>git commit -m "Add hello.py"
    # [main c57552b] Add hello.py
    #  1 file changed, 10 insertions(+)
    #  create mode 100644 hello.py
# Делаем push (step 3): C:\My projects\Туториалы\Git_tuts\git_test\git_tut>git push
    # Enumerating objects: 4, done.
    # Counting objects: 100% (4/4), done.
    # Delta compression using up to 8 threads
    # Compressing objects: 100% (3/3), done.
    # Writing objects: 100% (3/3), 648 bytes | 648.00 KiB/s, done.
    # Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
    # To https://github.com/LeshenShow/git_tut.git
    #    ac9c767..c57552b  main -> main
# Скачиваем наш новый файл на другом компе:  (важно указать cd папка-на другом компе)
#! C:\My projects\Туториалы\Git_tuts\git_2_clone\git_tut>git pull
# remote: Enumerating objects: 4, done.
# remote: Counting objects: 100% (4/4), done.
# remote: Compressing objects: 100% (3/3), done.
# remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
# Unpacking objects: 100% (3/3), 628 bytes | 125.00 KiB/s, done.
# From https://github.com/LeshenShow/git_tut
#    ac9c767..c57552b  main       -> origin/main
# Updating ac9c767..c57552b
# Fast-forward
#  hello.py | 10 ++++++++++
#  1 file changed, 10 insertions(+)
#  create mode 100644 hello.py

### git add -A -добавить все изменения