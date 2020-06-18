#!/usr/bin/bash

find . -name "*.so" -exec ls -lv {} \;
find . -name "*.so" -exec rm -rfv {} \;

find . -name "*.out" -exec ls -lv {} \;
find . -name "*.out" -exec rm -rfv {} \;


find . -name "*.class" -exec ls -lv {} \;
find . -name "*.class" -exec rm -rfv {} \;

find . -name "*.exe" -exec ls -lv {} \;
find . -name "*.exe" -exec rm -rfv {} \;

find . -name "*.dll" -exec ls -lv {} \;
find . -name "*.dll" -exec rm -rfv {} \;

find . -name "*.o" -exec ls -lv {} \;
find . -name "*.o" -exec rm -rfv {} \;

deleteExt=( md cpp c php py java txt lisp o dll pyc )

for i in "${deleteExt[@]}"
do
    find . -name "*.$i~" -exec ls -lv {} \;
    find . -name "*.$i#" -exec ls -lv {} \;
    find . -name "*.$i~" -exec rm -rfv {} \;
    find . -name "*.$i#" -exec rm -rfv {} \;
    find . -name "*.pyc" -exec ls -lv {} \;
    find . -name "*.pyc" -exec rm -rfv {} \;
done

find . -name "CMakeCache.txt" -exec ls -lv {} \;
find . -name "CMakeCache.txt" -exec rm -rfv {} \;
find . -name "cmake_install.cmake" -exec ls -lv {} \;
find . -name "cmake_install.cmake" -exec rm -rfv {} \;

#find . -name "Makefile" -exec ls -lv {} \;
#find . -name "Makefile" -exec rm -rfv {} \;
find . -type d -iname "CMakeFiles" -exec ls -lv {} \;
find . -type d -iname "CMakeFiles" -exec rm -rfv {} \;

#To revert some files from git
#git checkout -- c/threads/bogotobogodotcom/Makefile
#git checkout -- data_structure_n_algorithm/Searching/hashtable/www6_uniovi_es/Makefile

exit 0
