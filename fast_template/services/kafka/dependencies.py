from aiokafka import AIOKafkaProducer
from fastapi import Request
from taskiq import TaskiqDepends


def get_kafka_producer(
    request: Request = TaskiqDepends(),
) -> AIOKafkaProducer:  # pragma: no cover
    """
    Returns kafka producer.

    :param request: current request.
    :return: kafka producer from the state.
    """
    return request.app.state.kafka_producer
