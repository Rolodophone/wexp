import psutil
from django.shortcuts import render
from .byte_converter import bytes2human


def main_view(request):
	cpu = psutil.cpu_percent(interval=0.2, percpu=True)
	cpu_total = psutil.cpu_percent(interval=0.2, percpu=False)
	memory = psutil.virtual_memory()

	context = {
		'cpu_core_percents': cpu,
		'cpu_total_percent': cpu_total,  # TODO
		'memory_used': bytes2human(memory.used),
		'memory_total': bytes2human(memory.total),
		'memory_percent': memory.percent
	}

	return render(request, 'main_view.html', context=context)
