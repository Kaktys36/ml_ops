#!/bin/bash

JENKINS_HOME="$JENKINS_HOME"

BUILD_DIR="/build"

mkdir -p "$BUILD_DIR" || { echo "Ошибка при создании каталога 'build'."; exit 1; }

if [ ! -d "$JENKINS_HOME/workspace/MLOps" ]; then
    echo "Каталог MLOps не найден в директории Jenkins Home."
    exit 1
fi

cp -R "$JENKINS_HOME/workspace/MLOps/"* "$BUILD_DIR" || { echo "Ошибка при копировании содержимого MLOps."; exit 1; }

python3 -m venv "$BUILD_DIR/venv" || { echo "Ошибка при создании виртуального окружения."; exit 1; }

source "$BUILD_DIR/venv/bin/activate" || { echo "Ошибка при активации виртуального окружения."; exit 1; }

pip install -r "$BUILD_DIR/2/requirements.txt" || { echo "Ошибка при установке зависимостей."; exit 1; }

cd "$BUILD_DIR/2/src" || { echo "Не удалось перейти в каталог src"; exit 1; }

echo "Запуск создания данных"
python new_data.py || { echo "Ошибка при выполнении new_data.py"; exit 1; }

echo "Запуск предобработки данных"
python preprocess.py || { echo "Ошибка при выполнении preprocess.py"; exit 1; }

echo "Запуск подготовки и обучения модели"
python model_prep.py || { echo "Ошибка при выполнении model_prep.py"; exit 1; }

echo "Запуск тестирования модели"
python test_model.py || { echo "Ошибка при выполнении test_model.py"; exit 1; }