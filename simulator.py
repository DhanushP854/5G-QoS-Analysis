import random
from datetime import datetime, timedelta

NUMBER_OF_MEASUREMENTS = 200

metric_id = 102
start_time = datetime(2026, 8, 2, 10, 0, 0)

with open("network_data_realistic.sql", "w") as file:

    for i in range(NUMBER_OF_MEASUREMENTS):

        # Select an existing user
        user_id = random.randint(1, 20)

        # Generate network load
        network_load = random.uniform(20, 95)

        # Throughput decreases as network load increases
        base_throughput = 150 - (network_load * 0.9)
        throughput = base_throughput + random.uniform(-10, 10)

        # Latency increases as network load increases
        base_latency = 15 + (network_load * 0.8)
        latency = base_latency + random.uniform(-5, 10)

        # Packet loss increases with network load
        base_packet_loss = network_load / 20
        packet_loss = base_packet_loss + random.uniform(-1, 2)

        # Generate signal parameters
        sinr = random.uniform(5, 25)
        rsrp = random.uniform(-110, -70)

        # Prevent unrealistic negative values
        throughput = max(5, throughput)
        latency = max(5, latency)
        packet_loss = max(0, packet_loss)

        measurement_time = start_time + timedelta(minutes=i * 5)

        sql = f"""
INSERT INTO network_metrics (
    metric_id,
    user_id,
    measurement_time,
    sinr,
    rsrp,
    throughput_mbps,
    latency_ms,
    packet_loss,
    network_load
)
VALUES (
    {metric_id},
    {user_id},
    TO_DATE(
        '{measurement_time.strftime("%Y-%m-%d %H:%M:%S")}',
        'YYYY-MM-DD HH24:MI:SS'
    ),
    {sinr:.2f},
    {rsrp:.2f},
    {throughput:.2f},
    {latency:.2f},
    {packet_loss:.2f},
    {network_load:.2f}
);
"""

        file.write(sql)

        metric_id += 1

    file.write("\nCOMMIT;\n")

print("Realistic 5G simulation completed.")
print("200 measurements generated.")
print("SQL file created: network_data_realistic.sql")
