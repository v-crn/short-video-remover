# delete-video

指定の再生時間（デフォルトでは60秒）以下の動画を削除する Python ファイル。

## 使い方

delete_video.py と同じ階層に動画ファイルがある場合

```sh
python delete_video.py
```

### オプション引数

- `--dir`: 動画ファイルの存在するディレクトリ

```sh
python delete_video.py --dir=/mnt/e/Amusements/VideoEditting/materials/Videos
```

-- `--time`: 削除する再生時間上限の指定

```sh
python delete_video.py --dir=/mnt/e/Amusements/VideoEditting/materials/Videos --time=30
```
