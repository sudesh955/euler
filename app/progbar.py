import sys
from time import perf_counter, sleep
from typing import Generator, Generic, Iterable, Optional, TypeVar

T = TypeVar("T")


class progbar(Generic[T]):
	def __init__(
		self,
		items: Optional[Iterable[T]] = None,
		total: int = 0,
		current: int = 0,
		refresh_interval: float = 1.0,
		width: int = 30,
	) -> None:
		super().__init__()

		self.items = items
		if items is not None and total == 0:
			try:
				total = len(items)  # type: ignore
			except Exception:
				pass
		self.total = total
		self.current = current
		self.refresh_interval = refresh_interval
		self.width = width
		self.started_at = perf_counter()
		self.last_refreshed_at = perf_counter()
		self.time_per_step = 0

	def add(self, steps: int) -> int:
		current = self.current
		self.update(steps + current)
		return steps + current

	def update(self, current: int) -> None:
		if current <= self.current:
			return
		self.current = current
		now = perf_counter()
		if now - self.last_refreshed_at < self.refresh_interval:
			return
		self.refresh(now)

	def refresh(self, now: float) -> None:
		total = self.total
		current = self.current
		time_per_step = (now - self.started_at) / current
		speed = self.format_time_per_step(time_per_step)
		if total == 0 or current > total:
			output = f"{current}/Unknown {speed}"
		else:
			width = self.width
			prog = round((current * width) / total)
			eta = self.format_duration((total - current) * time_per_step)
			bar = "=" * prog + ">" + "." * (width - 1 - prog)
			output = f"{current}/{total} [{bar}] ETA: {eta} @ {speed}"
		self.write(output)
		self.last_refreshed_at = now

	def write(self, output: str) -> None:
		print(output)
		sys.stdout.flush()

	def close(self) -> None:
		current = self.current
		bar = "=" * self.width
		duration = perf_counter() - self.started_at
		formatted_duration = self.format_duration(duration)
		time_per_step = duration / (current if current != 0 else 1)
		speed = self.format_time_per_step(time_per_step)
		output = f"{current}/{self.total} [{bar}] {formatted_duration} @ {speed}\n"
		self.write(output)

	def __iter__(self) -> Generator[T, None, None]:
		assert self.items is not None
		self.current = current = -1
		refresh_interval = self.refresh_interval
		last_refreshed_at = perf_counter()
		for current, item in enumerate(self.items):
			yield item
			now = perf_counter()
			if now - last_refreshed_at > refresh_interval:
				self.current = current + 1
				self.refresh(now)
				last_refreshed_at = now
		self.current = current + 1
		self.close()

	@staticmethod
	def format_time_per_step(value: float) -> str:
		if value >= 1.0:
			return f"{round(value)}s/step"
		elif value >= 1e-3:
			return f"{round(value * 1e3)}ms/step"
		else:
			return f"{round(value * 1e6)}us/step"

	@staticmethod
	def format_duration(value: float) -> str:
		hrs = int(value / 3600)
		mins = int((value - hrs * 3600) / 60)
		secs = round(value - hrs * 3600 - mins * 60)
		if hrs != 0:
			return f"{hrs}:{mins:02}:{secs:02}"
		elif mins != 0:
			return f"{mins:02}:{secs:02}"
		else:
			return f"{secs:02}"


def pref():
	t = perf_counter()
	for _ in range(1000000):
		pass
	print(perf_counter() - t)

	t = perf_counter()
	for _ in progbar(range(1000000)):
		pass
	print(perf_counter() - t)


def accuracy():
	"this is should print values n*5 for 5 secs"
	for _ in progbar(range(25)):
		sleep(0.2)


def correct():
	def f(n):
		for i in range(n):
			yield i

	for _ in progbar(range(0)):
		pass
	for _ in progbar(range(10)):
		pass

	for _ in progbar(f(0)):
		pass
	for _ in progbar(f(10)):
		pass
