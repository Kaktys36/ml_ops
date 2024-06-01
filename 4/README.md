# MLOps. Практическое задание №4


### Выполнено практическое задание
    В рамках данного задания выполнены все основные операции с dvc. 
    Полученные теоретические знания, закрепленены, практическими действиями.

### Ссылки
- [Репозиторий с кодом](https://github.com/nocsland/urfu_mlops/tree/master/lab4)
- [README](https://github.com/nocsland/urfu_mlops/blob/master/lab4/README.md)
- [Функции для предобработки данных](https://github.com/nocsland/urfu_mlops/tree/master/lab4/src)
- [Облачное хранилище датасетов](https://drive.google.com/drive/folders/1kn2TH2myV6_gXmE1dFD76KoezClE1ygp?usp=sharing)
- [файл DVC для отслеживания версий данных](https://github.com/nocsland/urfu_mlops/blob/master/lab4/datasets.dvc)

### Дополнения
Для переключения между версиями датасета использовал следующую конструкцию
```
git log --oneline
git checkout <commit_id>
dvc pull
```
Для возвращения к текущей актуальной версии датасета
```
git checkout master
dvc pull
```