import os
import subprocess

print("**********************************************************************************\n"
      + "此脚本用于批量将字幕嵌入到mkv视频文件中\n************************************************"
        "**********************************")

video_dir = input(r"请输入视频目录路径：")
subtitle_dir = input(r"请输入字幕目录路径：")
output_dir = input(r"请输入输出目录路径：")
video_extension = r".mkv"
subtitle_extension = input(r"请输入字幕文件扩展名（例如：.sc.ass）：")
mkvmerge_dir = r"E:\green\mkvtoolnix"  # 请自行修改目录

print("\n\n视频目录：" + video_dir, "\n字幕目录：" + subtitle_dir, "\n输出目录：" + output_dir, "\n视频后缀："
      + video_extension, "\n字幕后缀：" + subtitle_extension, "\nmkvmerge目录：" + mkvmerge_dir + "\n\n")

# 获取视频文件列表（不包括子目录）
video_files = [file for file in os.listdir(video_dir) if
               file.endswith(video_extension) and os.path.isfile(os.path.join(video_dir, file))]

for video_file in video_files:
    base_name = os.path.splitext(video_file)[0]  # 去除扩展名的文件名
    video_path = os.path.join(video_dir, video_file)
    subtitle_file = os.path.join(subtitle_dir, base_name + subtitle_extension)
    output_file = os.path.join(output_dir, "output_" + video_file)  # 构建输出文件路径
    if os.path.exists(subtitle_file):
        # 构建 mkvmerge 执行命令，使用提供的 mkvmerge 目录
        mkvmerge_command = os.path.join(mkvmerge_dir, "mkvmerge.exe")
        # mkvmerge命令参数，可根据需要自行修改
        command = [
            mkvmerge_command,
            "--ui-language", "zh_CN",
            "--output", f'"{output_file}"',
            f'"{video_path}"',
            f'"{subtitle_file}"',
        ]

        # 执行命令
        # 使用 subprocess.run() 来执行命令
        subprocess.run(" ".join(command), shell=True)
        print("")

print("处理完成！")
