from unittest.mock import Mock, patch

import pytest
from poke_env.battle import AbstractBattle, DoubleBattle
from poke_env.player import DefaultBattleOrder, DoubleBattleOrder
from src.shiny_venipede.players.metronome_player import MetronomePlayer
from tests.support.builders.double_battle_order_builder import DoubleBattleOrderBuilder


def test_get_orders_returns_joined_orders(
    default_double_battle: DoubleBattle, metronome_player: MetronomePlayer
):
    joined_orders = [DoubleBattleOrderBuilder().build()]
    with patch.object(DoubleBattleOrder, "join_orders") as mock:
        mock.return_value = joined_orders
        orders = metronome_player._get_orders(default_double_battle)
        assert orders == joined_orders


def test_get_order_handles_exception(
    default_double_battle: DoubleBattle,
    metronome_player: MetronomePlayer,
):
    with patch.object(DoubleBattleOrder, "join_orders") as mock:
        mock.side_effect = Exception("test_error")
        orders = metronome_player._get_orders(default_double_battle)
        assert orders == []


async def test_choose_move_raises_error_for_non_double_battle(
    metronome_player: MetronomePlayer,
):
    battle = Mock(spec=AbstractBattle)
    with pytest.raises(TypeError):
        await metronome_player.choose_move(battle)


async def test_choose_move_returns_random_order(
    default_double_battle: DoubleBattle, metronome_player: MetronomePlayer
):
    order_1 = DoubleBattleOrderBuilder().build()
    order_2 = DoubleBattleOrderBuilder().build()
    with patch.object(metronome_player, "_get_orders") as player_mock:
        player_mock.return_value = [order_1, order_2]
        with patch("random.choice") as choice_mock:
            choice_mock.return_value = order_2
            output_order = await metronome_player.choose_move(default_double_battle)
            assert output_order == order_2


async def test_choose_move_fallback_when_no_orders(
    default_double_battle: DoubleBattle,
    empty_double_battle: DoubleBattle,
    metronome_player: MetronomePlayer,
):
    with patch.object(metronome_player, "_get_orders") as move:
        move.return_value = empty_double_battle
        orders = await metronome_player.choose_move(default_double_battle)
        assert isinstance(orders, DoubleBattleOrder)
        assert isinstance(orders.first_order, DefaultBattleOrder)
        assert isinstance(orders.second_order, DefaultBattleOrder)


async def test_choose_move_handles_exception(
    default_double_battle: DoubleBattle,
    metronome_player: MetronomePlayer,
):
    with patch.object(metronome_player, "_get_orders") as move:
        move.side_effect = Exception("test_error")
        orders = await metronome_player.choose_move(default_double_battle)
        assert isinstance(orders, DoubleBattleOrder)
        assert isinstance(orders.first_order, DefaultBattleOrder)
        assert isinstance(orders.second_order, DefaultBattleOrder)
