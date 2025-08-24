import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()


async def main_for_server():
    '''
    Streams - примитив для работы с сетевым подключением. Позволяет 
    создать как клиент, так и сервер. Поддерживает чтение и отправку 
    данных 
    '''
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888
    )
    addrs = ', '.join(str(sock.getsockname) for sock in server.sockets)
    print(addrs)

    async with server:
        await server.serve_forever()
    
asyncio.run(main_for_server())