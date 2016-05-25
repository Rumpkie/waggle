#!/bin/bash

echo "--- Web documents initializing..."

if [ $# -eq 0 ]
  then
    echo "No arguments inserted! - use 'make docs'."
    exit 1
fi

FILE="$1"

OBJ_FILES=($(awk -F '[:]' '{print $2}' ${FILE}))
OUT_FILES=($(awk -F '[:]' '{print $1}' ${FILE}))

ROOT_DIR=../
WEB_DIR=${ROOT_DIR}web/
TEMP_DIR=${WEB_DIR}tmp/

mkdir -p ${TEMP_DIR}

echo "--- Web documents generating..."
for i in ${!OUT_FILES[@]} ; do
  from=${OBJ_FILES[$i]}
  to=${OUT_FILES[$i]}
  name_to=$(basename ${to} ".html")
  dir_to=$(dirname ${to})
  
  echo "--- making a document ${to} <- ${from}"
  tmp=${TEMP_DIR}${name_to}
  cp ${ROOT_DIR}${from} ${tmp}

  #sed -i 's/.md/.html/g' $(OBJ_DIR)/$(patsubst %.html,%.md,$@)
  #pandoc -f markdown_github -t html ${tmp} -o ${WEB_DIR}${to}
  mkdir -p ${dir_to}
  pandoc -f markdown_github -t html ${tmp} -o ${to}

  echo "--- --- changing image links..."
  cnt=($(echo ${to} | awk -F/ '{ print NF - 1 }'))
  dir_from=$(dirname ${from})
  gotoroot=""
  for ((i=0;i<cnt;i++)); do
    gotoroot+="../"
  done
  gotoroot+="../"

  echo "# of direc: ${cnt}"
  echo "# of go back: ${gotoroot}${dir_from}"
  path_link=${gotoroot}${dir_from}/
  sed -i 's,<img src=",<img src="'"${path_link}"',g' ${to}

  #echo "--- --- changing page links..."
  #content=($(cat ${to})
  
done

