
import ffmpeg

url = 'rtsp://nutanix:test1234@192.168.100.21:554/Streaming/Channels/101'
stream = ffmpeg.input(url, c='copy')
stream = ffmpeg.output(stream, 'output-%03d.mp4', f='segment', segment_time=5)
ffmpeg.run(stream)

# stream = ffmpeg.input(url, c='copy')
#
# for x in range(5):
#     stream = ffmpeg.trim(stream, duration=5)
#     stream = ffmpeg.output(stream, f'output-{x}.mp4', t=5)
#     ffmpeg.run(stream)
#     print(f'stream {x} saved')

print('done')
