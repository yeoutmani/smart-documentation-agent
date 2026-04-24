from app.services.generator.generator_node import generator_node as gen_service

async def generator_node(state: dict):
    return await gen_service(state)