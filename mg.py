{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "FFmpeg for GDrive",
      "provenance": [],
      "collapsed_sections": [
        "EFOqhHG6hOVH",
        "CUq1_Dnegrs1",
        "KgNPvGccgwd8",
        "RDHuIkoi6l9a",
        "NQ0TxfKeghR8",
        "NObEcBWAJoaz",
        "FpJXJiRl6-gK",
        "SNDGdMRn3PA-",
        "2f-THZmDoOaY",
        "MSUasbRUDP3B",
        "9UagRtLPyKoQ",
        "GahMjYf8miNs",
        "7-3O4en4C4IL",
        "VRk2Ye1exWVA",
        "tozwpAhhnm69"
      ],
      "toc_visible": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sudo-ken/FFmpeg-for-GDrive/blob/master/FFmpeg_for_GDrive.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pety7rf841Dg",
        "colab_type": "text"
      },
      "source": [
        "# **<font color='blue'> Unrar, Unzip, Rar, Zip in GDrive - Shared by [SudoKen](https://www.youtube.com/channel/UCZq5YhZIR-250zX_MzkTbxA?sub_confirmation=1) </font>**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EFOqhHG6hOVH",
        "colab_type": "text"
      },
      "source": [
        "#__1. Install FFmpeg__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hFeE-qPuhTiK",
        "colab_type": "code",
        "cellView": "form",
        "colab": {}
      },
      "source": [
        "#@markdown <br><center><img src='https://github.com/RupomChowdhury/FC-for-GDrive/blob/main/ffmpeg.png' height=\"50\" alt=\"Gdrive-logo\"/></center>\n",
        "#@markdown <center><h3>Upgrade to v4.2.2</h3></center><br>\n",
        "from IPython.display import clear_output\n",
        "import os, urllib.request\n",
        "HOME = os.path.expanduser(\"~\")\n",
        "pathDoneCMD = f'{HOME}/doneCMD.sh'\n",
        "if not os.path.exists(f\"{HOME}/.ipython/ttmg.py\"):\n",
        "    hCode = \"https://raw.githubusercontent.com/sudo-ken/FFmpeg-for-GDrive/master/ttmg.py\"\n",
        "    urllib.request.urlretrieve(hCode, f\"{HOME}/.ipython/ttmg.py\")\n",
        "\n",
        "from ttmg import (\n",
        "    loadingAn,\n",
        "    textAn,\n",
        ")\n",
        "\n",
        "loadingAn(name=\"lds\")\n",
        "textAn(\"Installing Dependencies...\", ty='twg')\n",
        "os.system('pip install git+git://github.com/AWConant/jikanpy.git')\n",
        "os.system('add-apt-repository -y ppa:jonathonf/ffmpeg-4')\n",
        "os.system('apt-get update')\n",
        "os.system('apt install mediainfo')\n",
        "os.system('apt-get install ffmpeg')\n",
        "clear_output()\n",
        "print('Installation finished.')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CUq1_Dnegrs1",
        "colab_type": "text"
      },
      "source": [
        "#__2. Mount Google Drive__\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ojI73noUg1If",
        "colab_type": "code",
        "colab": {},
        "cellView": "form"
      },
      "source": [
        "#@markdown <br><center><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Google_Drive_logo.png/600px-Google_Drive_logo.png' height=\"50\" alt=\"Gdrive-logo\"/></center>\n",
        "#@markdown <center><h3>Mount GDrive to /content/drive</h3></center><br>\n",
        "MODE = \"MOUNT\" #@param [\"MOUNT\", \"UNMOUNT\"]\n",
        "#Mount your Gdrive! \n",
        "from google.colab import drive\n",
        "drive.mount._DEBUG = False\n",
        "if MODE == \"MOUNT\":\n",
        "  drive.mount('/content/drive', force_remount=True)\n",
        "elif MODE == \"UNMOUNT\":\n",
        "  try:\n",
        "    drive.flush_and_unmount()\n",
        "  except ValueError:\n",
        "    pass\n",
        "  get_ipython().system_raw(\"rm -rf /root/.config/Google/DriveFS\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KgNPvGccgwd8",
        "colab_type": "text"
      },
      "source": [
        "#__3. Run FFmpeg Scripts (Convert, Edit, Trim + more)__"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RDHuIkoi6l9a",
        "colab_type": "text"
      },
      "source": [
        "###__Display Media File Metadata__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Sv8au_RO6WUs",
        "colab_type": "code",
        "cellView": "form",
        "colab": {}
      },
      "source": [
        "import os, sys, re\n",
        "\n",
        "media_file_path = \"\" #@param {type:\"string\"}\n",
        "\n",
        "os.environ['inputFile'] = media_file_path\n",
        "\n",
        "!ffmpeg -i \"$inputFile\" -hide_banner"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "X4yIG_nqYAoH",
        "colab_type": "text"
      },
      "source": [
        "> *You can ignore the* \"`At least one output file must be specified`\" *error after running this.*\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NQ0TxfKeghR8",
        "colab_type": "text"
      },
      "source": [
        "###__Convert Video File ➔ .mp4 (Lossless)__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ls4O5VLwief-",
        "colab_type": "code",
        "cellView": "form",
        "colab": {}
      },
      "source": [
        "import os, sys, re\n",
        "\n",
        "video_file_path = \"\" #@param {type:\"string\"}\n",
        "\n",
        "output_file_path = re.search(\"^[\\/].+\\/\", video_file_path)\n",
        "output_file_path_raw = output_file_path.group(0)\n",
        "delsplit = re.search(\"\\/(?:.(?!\\/))+$\", video_file_path)\n",
        "filename = re.sub(\"^[\\/]\", \"\", delsplit.group(0))\n",
        "filename_raw = re.sub(\".{4}$\", \"\", filename)\n",
        "file_extension = re.search(\".{3}$\", filename)\n",
        "file_extension_raw = file_extension.group(0)\n",
        "\n",
        "os.environ['inputFile'] = video_file_path\n",
        "os.environ['outputPath'] = output_file_path_raw\n",
        "os.environ['fileName'] = filename_raw\n",
        "os.environ['fileExtension'] = file_extension_raw\n",
        "\n",
        "!ffmpeg -hide_banner -i \"$inputFile\" -c copy -strict -2 \"$outputPath\"/\"$fileName\".mp4"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "NObEcBWAJoaz"
      },
      "source": [
        "###__Convert Video File ➔ .mkv (Lossless)__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "cellView": "form",
        "id": "zsx4JFLRJoa0",
        "colab": {}
      },
      "source": [
        "import os, sys, re\n",
        "\n",
        "video_file_path = \"\" #@param {type:\"string\"}\n",
        "\n",
        "output_file_path = re.search(\"^[\\/].+\\/\", video_file_path)\n",
        "output_file_path_raw = output_file_path.group(0)\n",
        "delsplit = re.search(\"\\/(?:.(?!\\/))+$\", video_file_path)\n",
        "filename = re.sub(\"^[\\/]\", \"\", delsplit.group(0))\n",
        "filename_raw = re.sub(\".{4}$\", \"\", filename)\n",
        "file_extension = re.search(\".{3}$\", filename)\n",
        "file_extension_raw = file_extension.group(0)\n",
        "\n",
        "os.environ['inputFile'] = video_file_path\n",
        "os.environ['outputPath'] = output_file_path_raw\n",
        "os.environ['fileName'] = filename_raw\n",
        "os.environ['fileExtension'] = file_extension_raw\n",
        "\n",
        "!ffmpeg -hide_banner -i \"$inputFile\" -c copy -strict -2 \"$outputPath\"/\"$fileName\".mkv"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FpJXJiRl6-gK",
        "colab_type": "text"
      },
      "source": [
        "###__Trim Video File (Lossless)__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iFBUeQhn7QTc",
        "colab_type": "code",
        "cellView": "form",
        "colab": {}
      },
      "source": [
        "import os, sys, re\n",
        "\n",
        "video_file_path = \"\" #@param {type:\"string\"}\n",
        "start_time = \"00:00:00.000\" #@param {type:\"string\"}\n",
        "end_time = \"00:01:00.000\" #@param {type:\"string\"}\n",
        "\n",
        "output_file_path = re.search(\"^[\\/].+\\/\", video_file_path)\n",
        "output_file_path_raw = output_file_path.group(0)\n",
        "delsplit = re.search(\"\\/(?:.(?!\\/))+$\", video_file_path)\n",
        "filename = re.sub(\"^[\\/]\", \"\", delsplit.group(0))\n",
        "filename_raw = re.sub(\".{4}$\", \"\", filename)\n",
        "file_extension = re.search(\".{3}$\", filename)\n",
        "file_extension_raw = file_extension.group(0)\n",
        "\n",
        "os.environ['inputFile'] = video_file_path\n",
        "os.environ['outputPath'] = output_file_path_raw\n",
        "os.environ['startTime'] = start_time\n",
        "os.environ['endTime'] = end_time\n",
        "os.environ['fileName'] = filename_raw\n",
        "os.environ['fileExtension'] = file_extension_raw\n",
        "\n",
        "!ffmpeg -hide_banner -i \"$inputFile\" -ss \"$startTime\" -to \"$endTime\" -c copy \"$outputPath\"/\"$fileName\"-TRIM.\"$fileExtension\""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "SNDGdMRn3PA-"
      },
      "source": [
        "###__Crop Video__"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KFcIThDuBii_",
        "colab_type": "text"
      },
      "source": [
        "<h3> Crop Variables Explanation:\n",
        "\n",
        "* `out_width` = The width of your cropped video file.\n",
        "* `out_height` = The height of your cropped video file.\n",
        "* `starting_position_x` & `starting_position_y` = These values define the x & y coordinates of the top left corner of your original video to start cropping from.\n",
        "\n",
        "###### *Example: For cropping the black bars from a video that looked like* [this](https://i.imgur.com/ud8nbvT.png):\n",
        "* *For your starting coordinates* (`x` , `y`) *you would use* (`0` , `138`).\n",
        "* *For* `out_width` *you would use* `1920`. *And for* `out_height` *you would use `804`.*\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "cellView": "form",
        "id": "CEHi5EMm9lXG",
        "colab": {}
      },
      "source": [
        "import os, sys, re\n",
        "\n",
        "video_file_path = \"\" #@param {type:\"string\"}\n",
        "out_width = \"1920\" #@param {type:\"string\"}\n",
        "out_height = \"804\" #@param {type:\"string\"}\n",
        "starting_position_x = \"0\" #@param {type:\"string\"}\n",
        "starting_position_y = \"138\" #@param {type:\"string\"}\n",
        "\n",
        "output_file_path = re.search(\"^[\\/].+\\/\", video_file_path)\n",
        "output_file_path_raw = output_file_path.group(0)\n",
        "delsplit = re.search(\"\\/(?:.(?!\\/))+$\", video_file_path)\n",
        "filename = re.sub(\"^[\\/]\", \"\", delsplit.group(0))\n",
        "filename_raw = re.sub(\".{4}$\", \"\", filename)\n",
        "file_extension = re.search(\".{3}$\", filename)\n",
        "file_extension_raw = file_extension.group(0)\n",
        "\n",
        "os.environ['inputFile'] = video_file_path\n",
        "os.environ['outputPath'] = output_file_path_raw\n",
        "os.environ['outWidth'] = out_width\n",
        "os.environ['outHeight'] = out_height\n",
        "os.environ['positionX'] = starting_position_x\n",
        "os.environ['positionY'] = starting_position_y\n",
        "os.environ['fileName'] = filename_raw\n",
        "os.environ['fileExtension'] = file_extension_raw\n",
        "\n",
        "!ffmpeg -hide_banner -i \"$inputFile\" -filter:v \"crop=$outWidth:$outHeight:$positionX:$positionY\" \"$outputPath\"/\"$fileName\"-CROP.\"$fileExtension\""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "2f-THZmDoOaY"
      },
      "source": [
        "###__Extract Audio from Video File (Lossless)__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nSeO98YQoTJe",
        "colab_type": "code",
        "cellView": "form",
        "colab": {}
      },
      "source": [
        "import os, sys, re\n",
        "\n",
        "video_file_path = \"\" #@param {type:\"string\"}\n",
        "output_file_extension = 'm4a' #@param [\"m4a\", \"mp3\", \"opus\", \"flac\", \"wav\"]\n",
        "\n",
        "delsplit = re.search(\"\\/(?:.(?!\\/))+$\", video_file_path)\n",
        "output_file_path = re.search(\"^[\\/].+\\/\", video_file_path)\n",
        "filename = re.sub(\"^[\\/]\", \"\", delsplit.group(0))\n",
        "filename_raw = re.sub(\".{4}$\", \"\", filename)\n",
        "\n",
        "os.environ['inputFile'] = video_file_path\n",
        "os.environ['outputPath'] = output_file_path.group(0)\n",
        "os.environ['fileName'] = filename_raw\n",
        "os.environ['fileType'] = output_file_extension\n",
        "\n",
        "!ffmpeg -hide_banner -i \"$inputFile\" -vn -c:a copy \"$outputPath\"/\"$fileName\"-audio.\"$fileType\""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MSUasbRUDP3B",
        "colab_type": "text"
      },
      "source": [
        "###__Re-encode a Video to a Different Resolution__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nd2LvSRZCxRe",
        "colab_type": "code",
        "cellView": "form",
        "colab": {}
      },
      "source": [
        "import os, sys, re\n",
        "\n",
        "video_file_path = '' #@param {type:\"string\"}\n",
        "resolution = '1080p' #@param [\"2160p\", \"1440p\", \"1080p\", \"720p\", \"480p\", \"360p\", \"240p\"]\n",
        "file_type = 'mp4' #@param [\"mkv\", \"mp4\"]\n",
        "\n",
        "delsplit = re.search(\"\\/(?:.(?!\\/))+$\", video_file_path)\n",
        "testsplit = video_file_path.split(\"/\")\n",
        "filename = re.sub(\"^[\\/]\", \"\", delsplit.group(0))\n",
        "filename_raw = re.sub(\".{4}$\", \"\", filename)\n",
        "resolution_raw = re.search(\"[^p]{3,4}\", resolution)\n",
        "output_file_path = re.search(\"^[\\/].+\\/\", video_file_path)\n",
        "\n",
        "os.environ['inputFile'] = video_file_path\n",
        "os.environ['outputPath'] = output_file_path.group(0)\n",
        "os.environ['fileName'] = filename_raw\n",
        "os.environ['fileType'] = file_type\n",
        "os.environ['resolutionHeight'] = resolution_raw.group(0)\n",
        "\n",
        "!ffmpeg -hide_banner -i \"$inputFile\" -vf \"scale=-1:\"$resolutionHeight\"\" -c:a copy -strict experimental \"$outputPath\"/\"$fileName\"-\"$resolutionHeight\"p.\"$fileType\""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "9UagRtLPyKoQ"
      },
      "source": [
        "###__Extract Individual Frames from Video__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "cellView": "form",
        "id": "jTnByMhAyKoF",
        "colab": {}
      },
      "source": [
        "#@markdown This will create a folder in the same directory titled \"`Extracted Frames`\"\n",
        "#@markdown - [Example](https://i.imgur.com/yPDk1hO.png) of output folder\n",
        "import os, sys, re\n",
        "\n",
        "video_file_path = \"\" #@param {type:\"string\"}\n",
        "start_time = \"00:01:00.000\" #@param {type:\"string\"}\n",
        "end_time = \"00:01:05.000\" #@param {type:\"string\"}\n",
        "frame_rate = \"23.976\" #@param {type:\"string\"}\n",
        "\n",
        "output_file_path = re.search(\"^[\\/].+\\/\", video_file_path)\n",
        "output_file_path_raw = output_file_path.group(0)\n",
        "delsplit = re.search(\"\\/(?:.(?!\\/))+$\", video_file_path)\n",
        "filename = re.sub(\"^[\\/]\", \"\", delsplit.group(0))\n",
        "filename_raw = re.sub(\".{4}$\", \"\", filename)\n",
        "file_extension = re.search(\".{3}$\", filename)\n",
        "file_extension_raw = file_extension.group(0)\n",
        "\n",
        "os.environ['inputFile'] = video_file_path\n",
        "os.environ['outputPath'] = output_file_path_raw\n",
        "os.environ['startTime'] = start_time\n",
        "os.environ['endTime'] = end_time\n",
        "os.environ['frameRate'] = frame_rate\n",
        "os.environ['fileName'] = filename_raw\n",
        "os.environ['fileExtension'] = file_extension_raw\n",
        "\n",
        "!mkdir \"$outputPath\"/\"Extracted Frames\"\n",
        "!ffmpeg -hide_banner -i \"$inputFile\" -ss \"$startTime\" -to \"$endTime\" -r \"$frameRate\"/1 \"$outputPath\"/\"Extracted Frames\"/frame%04d.png"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "GahMjYf8miNs"
      },
      "source": [
        "###__Generate Thumbnails - Preview from Video (3x2)__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "cellView": "form",
        "id": "J2u-Rha8miNy",
        "colab": {}
      },
      "source": [
        "#@markdown Example of output image: https://i.imgur.com/0ymP144.png <br>\n",
        "import os, sys, re\n",
        "\n",
        "video_file_path = \"\" #@param {type:\"string\"}\n",
        "output_file_type = 'png' #@param [\"png\", \"jpg\"]\n",
        "\n",
        "output_file_path = re.search(\"^[\\/].+\\/\", video_file_path)\n",
        "output_file_path_raw = output_file_path.group(0)\n",
        "delsplit = re.search(\"\\/(?:.(?!\\/))+$\", video_file_path)\n",
        "filename = re.sub(\"^[\\/]\", \"\", delsplit.group(0))\n",
        "filename_raw = re.sub(\".{4}$\", \"\", filename)\n",
        "file_extension = re.search(\".{3}$\", filename)\n",
        "file_extension_raw = file_extension.group(0)\n",
        "\n",
        "os.environ['inputFile'] = video_file_path\n",
        "os.environ['outputPath'] = output_file_path_raw\n",
        "os.environ['outputExtension'] = output_file_type\n",
        "os.environ['fileName'] = filename_raw\n",
        "os.environ['fileExtension'] = file_extension_raw\n",
        "\n",
        "!ffmpeg -hide_banner -i \"$inputFile\" -vframes 1 -q:v 2 -vf \"select=not(mod(n\\,200)),scale=-1:480,tile=3x2\" -an \"$outputPath\"/\"$fileName\"_thumbnails.\"$outputExtension\""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7-3O4en4C4IL",
        "colab_type": "text"
      },
      "source": [
        "###__Convert Audio Filetype (mp3, m4a, ogg, flac, etc.)__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aURlOf9BC1P3",
        "colab_type": "code",
        "cellView": "form",
        "colab": {}
      },
      "source": [
        "import os, sys, re\n",
        "\n",
        "audio_file_path = \"\" #@param {type:\"string\"}\n",
        "output_file_type = \"mp3\" #@param [\"mp3\", \"ogg\", \"m4a\", \"opus\", \"flac\", \"alac\", \"wav\"]\n",
        "\n",
        "output_file_path = re.search(\"^[\\/].+\\/\", audio_file_path)\n",
        "output_file_path_raw = output_file_path.group(0)\n",
        "delsplit = re.search(\"\\/(?:.(?!\\/))+$\", audio_file_path)\n",
        "filename = re.sub(\"^[\\/]\", \"\", delsplit.group(0))\n",
        "filename_raw = re.sub(\".{4}$\", \"\", filename)\n",
        "file_extension = re.search(\".{3}$\", filename)\n",
        "file_extension_raw = file_extension.group(0)\n",
        "\n",
        "os.environ['inputFile'] = audio_file_path\n",
        "os.environ['outputPath'] = output_file_path_raw\n",
        "os.environ['fileExtension'] = output_file_type\n",
        "os.environ['fileName'] = filename_raw\n",
        "\n",
        "!ffmpeg -hide_banner -i \"$inputFile\" \"$outputPath\"/\"$fileName\"converted.\"$fileExtension\""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "colab_type": "text",
        "id": "VRk2Ye1exWVA"
      },
      "source": [
        "###__Sharable Links of Randomly Extracted Frames from Video__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab_type": "code",
        "cellView": "form",
        "id": "BIGsgarfxWVI",
        "colab": {}
      },
      "source": [
        "import os, re, time, pathlib\n",
        "import urllib.request\n",
        "from IPython.display import clear_output\n",
        "\n",
        "Auto_UP_Gdrive = False  \n",
        "AUTO_MOVE_PATH = \"/content\" \n",
        "HOME = os.path.expanduser(\"~\")\n",
        "pathDoneCMD = f'{HOME}/doneCMD.sh'\n",
        "\n",
        "if not os.path.exists(f\"{HOME}/.ipython/ttmg.py\"):\n",
        "    hCode = \"https://raw.githubusercontent.com/biplobsd/\" \\\n",
        "                \"Google-Colab-CloudTorrent/master/res/ttmg.py\"\n",
        "    urllib.request.urlretrieve(hCode, f\"{HOME}/.ipython/ttmg.py\")\n",
        "\n",
        "from ttmg import (\n",
        "    runSh,\n",
        "    findProcess,\n",
        "    loadingAn,\n",
        "    updateCheck,\n",
        "    ngrok\n",
        ")\n",
        "\n",
        "video_file_path = \"\" #@param {type:\"string\"}\n",
        "\n",
        "output_file_path = re.search(\"^[\\/].+\\/\", video_file_path)\n",
        "output_file_path_raw = output_file_path.group(0)\n",
        "delsplit = re.search(\"\\/(?:.(?!\\/))+$\", video_file_path)\n",
        "filename = re.sub(\"^[\\/]\", \"\", delsplit.group(0))\n",
        "filename_raw = re.sub(\".{4}$\", \"\", filename)\n",
        "file_extension = re.search(\".{3}$\", filename)\n",
        "file_extension_raw = file_extension.group(0)\n",
        "\n",
        "os.environ['inputFile'] = video_file_path\n",
        "os.environ['outputPath'] = output_file_path_raw\n",
        "os.environ['fileName'] = filename_raw\n",
        "os.environ['fileExtension'] = file_extension_raw\n",
        "\n",
        "!mkdir -p \"/content/frames\"\n",
        "\n",
        "for i in range(10):\n",
        "    clear_output()\n",
        "    loadingAn()\n",
        "    print(\"Uploading Frames...\")\n",
        "\n",
        "%cd \"/content/frames\"\n",
        "!ffmpeg -hide_banner -ss 00:56.0 -i \"$inputFile\" -vframes 1 -q:v 1 -y \"/content/frames/frame1.png\"\n",
        "!curl --silent -F \"reqtype=fileupload\" -F \"fileToUpload=@frame1.png\" https://catbox.moe/user/api.php -o frame1.txt\n",
        "f1 = open('frame1.txt', 'r')\n",
        "%cd \"/content\"\n",
        "file_content1 = f1.read()\n",
        "\n",
        "%cd \"/content/frames\"\n",
        "!ffmpeg -hide_banner -ss 02:20.0 -i \"$inputFile\" -vframes 1 -q:v 1 -y \"/content/frames/frame2.png\"\n",
        "!curl --silent -F \"reqtype=fileupload\" -F \"fileToUpload=@frame2.png\" https://catbox.moe/user/api.php -o frame2.txt\n",
        "%cd \"/content/frames\"\n",
        "f2 = open('frame2.txt', 'r')\n",
        "%cd \"/content\"\n",
        "file_content2 = f2.read()\n",
        "\n",
        "clear_output()\n",
        "print (\"Screenshot URLs:\")\n",
        "print (\"1. \" + file_content1)\n",
        "print (\"2. \" + file_content2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tozwpAhhnm69",
        "colab_type": "text"
      },
      "source": [
        "\n",
        "###__MediaInfo__"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NTULRguzu0b0",
        "colab_type": "code",
        "cellView": "form",
        "colab": {}
      },
      "source": [
        "path = \"\" #@param {type:\"string\"}\n",
        "save_txt = True #@param {type:\"boolean\"}\n",
        "import os, uuid, re, IPython\n",
        "import ipywidgets as widgets\n",
        "import time\n",
        "\n",
        "from glob import glob\n",
        "from IPython.display import HTML, clear_output\n",
        "from google.colab import output, drive\n",
        "\n",
        "def mediainfo():\n",
        "  display(HTML(\"<br>\"))\n",
        "#   print(path.split(\"/\")[::-1][0])\n",
        "  display(HTML(\"<br>\"))\n",
        "#   media = !mediainfo \"$path\"\n",
        "#   media = \"\\n\".join(media).replace(os.path.dirname(path)+\"/\", \"\")\n",
        "  get_ipython().system_raw(\"\"\"mediainfo --LogFile=\"/root/.nfo\" \"$path\" \"\"\")\n",
        "  with open('/root/.nfo', 'r') as file:\n",
        "    media = file.read()\n",
        "    media = media.replace(os.path.dirname(path)+\"/\", \"\")\n",
        "  print(media)\n",
        "  get_ipython().system_raw(\"rm -f '/root/.nfo'\")\n",
        "  \n",
        "  if save_txt:\n",
        "    txt = path.rpartition('.')[0] + \".txt\"\n",
        "    if os.path.exists(txt):\n",
        "      get_ipython().system_raw(\"rm -f '$txt'\")\n",
        "    !curl -s https://pastebin.com/raw/TV8Byydt -o \"$txt\"\n",
        "    with open(txt, 'a+') as file:\n",
        "      file.write(\"\\n\\n\")\n",
        "      file.write(media)\n",
        "\n",
        "while not os.path.exists(\"/content/drive\"):\n",
        "  try:\n",
        "    drive.mount(\"/content/drive\")\n",
        "    clear_output(wait=True)\n",
        "  except:\n",
        "    clear_output()\n",
        "    \n",
        "if not os.path.exists(\"/usr/bin/mediainfo\"):\n",
        "  get_ipython().system_raw(\"apt-get install mediainfo\")\n",
        "  \n",
        "mediainfo()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XDp_IAgx46fP",
        "colab_type": "text"
      },
      "source": [
        ""
      ]
    }
  ]
}
