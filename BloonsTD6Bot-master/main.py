import logging
import config
from map import DarkCastleMap
from tower import Tower
from bot import Bot
import dark_castle

if __name__ == '__main__':
    bot = dark_castle.DarkCastleBot()
    bot.main(required_hero='obyn')