import os
import asyncio
import sys

from asyncio.streams import StreamWriter, FlowControlMixin

reader, writer = None, None

async def stdio(loop=None):
    if loop is None:
        loop = asyncio.get_event_loop()

    reader = asyncio.StreamReader()
    reader_protocol = asyncio.StreamReaderProtocol(reader)

    writer_transport, writer_protocol = await loop.connect_write_pipe(FlowControlMixin, os.fdopen(0, 'wb'))
    writer = StreamWriter(writer_transport, writer_protocol, None, loop)

    await loop.connect_read_pipe(lambda: reader_protocol, sys.stdin)

    return reader, writer

async def async_input(message):
    if isinstance(message, str):
        message = message.encode('utf8')

    global reader, writer
    if (reader, writer) == (None, None):
        reader, writer = await stdio()

    writer.write(message)
    await writer.drain()

    line = await reader.readline()
    return line.decode('utf8').replace('\r', '').replace('\n', '')

if __name__ == "__main__":
    async def main():
        name = await async_input("What's your name? ")
        print("Hello, {}!".format(name))


    asyncio.get_event_loop().run_until_complete(main())