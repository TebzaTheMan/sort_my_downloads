# sort_my_downloads

A Python script to sort your downloaded files into categorised folders.

## Requirements

[watchdog](https://pypi.org/project/readme-cli/) => to be able to detect new files downloaded.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install sort_my_downloads.

```bash
pip install sort_my_downloads
```

## Usage

command to sort your downloads.

```bash
sort_my_downloads
```

command to start file watcher to sort new files that you will download.

```bash
sort_my_downloads watch
```

command to sort your downloads and watch for new files downloaded and sort them.

```bash
sort_my_downloads sort_and_watch
```

## How it works

| Folder        | File extension                                                                                         |
| ------------- | ------------------------------------------------------------------------------------------------------ |
| Documents     | doc , docx , html , htm , odt , pdf , xls , xlsx , ods , ppt , pptx , txt , csv , dotx , pgn           |
| Images        | jpg , png , gif , webp , tiff , psd , raw , bmp , heif , indd , jpeg                                   |
| Vector Images | svg , ai , eps , pdf                                                                                   |
| Music         | mp3 , m4a , aac , oga , flac , wav , pcm , aiff                                                        |
| Video         | webm , mpg , mp2 , mpeg , mpe , mpv , ogg , mp4 , m4p , m4v , avi , wmv , mov , qt , flv , swf , avchd |
| Compressed    | 7z , arj , deb , pkg , rar , rpm , tar.gz , z , zip , tgz                                              |
| Disc Images   | dmg , iso , toast , vcd                                                                                |
| Executables   | apk , bat , bin , cgi , pl , exe , jar , msi , py , wsf , app                                          |
| Fonts         | fnt , fon , otf , ttf                                                                                  |
| Other         | all other files that are not in above folders.                                                         |

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

1. [Fork it](https://github.com/TebzaTheMan/sort_my_downloads/fork)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

[MIT](https://choosealicense.com/licenses/mit/)
