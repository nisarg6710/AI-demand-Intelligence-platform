import time


class ETLMetrics:

    def __init__(self):

        self.start_time = None

        self.end_time = None

        self.rows_processed = 0

        self.chunks_processed = 0


    def start(self):

        self.start_time = time.perf_counter()


    def stop(self):

        self.end_time = time.perf_counter()


    def add_rows(self, rows):

        self.rows_processed += rows


    def add_chunk(self):

        self.chunks_processed += 1


    def execution_time(self):

        return self.end_time - self.start_time


    def throughput(self):

        if self.execution_time() == 0:

            return 0

        return self.rows_processed / self.execution_time()


    def summary(self):

        print("\n========== ETL SUMMARY ==========")

        print(f"Rows Processed : {self.rows_processed:,}")

        print(f"Chunks         : {self.chunks_processed}")

        print(f"Execution Time : {self.execution_time():.2f} sec")

        print(f"Throughput     : {self.throughput():,.2f} rows/sec")

        print("=================================\n")