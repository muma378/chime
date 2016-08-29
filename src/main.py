
import sys
import settings
from cli import RequestProxy

def main():
	from launcher import ChimeLauncher
	launcher = ChimeLauncher("Shujutang", "Chime")
	launcher.launch()


if __name__ == '__main__':
	recipe_path = sys.argv[1]
	rp = RequestProxy(settings.CHIME_SERVER_HOST)
	rp.push_task(recipe_path)