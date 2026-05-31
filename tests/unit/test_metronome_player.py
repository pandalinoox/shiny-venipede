from unittest.mock import Mock, patch

import pytest
from poke_env.battle import AbstractBattle, DoubleBattle
from poke_env.player import DefaultBattleOrder, DoubleBattleOrder
from tests.support.builders.double_battle_builder import DoubleBattleBuilder
from tests.support.builders.double_battle_order_builder import DoubleBattleOrderBuilder
from tests.support.utils.orders import (
    create_default_double_battle_order,
    create_double_battle_order_with_first,
    create_tera_order,
)

from shiny_venipede.players.metronome_player import MetronomePlayer


def test_get_orders_returns_joined_orders(
    default_double_battle: DoubleBattle,
    metronome_player: MetronomePlayer,
):
    joined_orders = [create_default_double_battle_order()]

    with patch.object(DoubleBattleOrder, "join_orders") as mock:
        mock.return_value = joined_orders

        result = metronome_player._get_orders(default_double_battle)

        assert result == joined_orders


def test_get_order_handles_exception(
    default_double_battle: DoubleBattle,
    metronome_player: MetronomePlayer,
):
    with patch.object(DoubleBattleOrder, "join_orders") as mock:
        mock.side_effect = Exception("test_error")

        result = metronome_player._get_orders(default_double_battle)

        assert result == []


def test_get_orders_returns_all_orders_when_cannot_tera(
    metronome_player: MetronomePlayer,
):
    joined_orders = [create_default_double_battle_order()]
    battle = DoubleBattleBuilder().with_can_tera(False).build()

    with patch.object(DoubleBattleOrder, "join_orders") as join_orders_mock:
        with patch.object(metronome_player._tera_strategy, "filter_orders"):
            join_orders_mock.return_value = joined_orders

            result = metronome_player._get_orders(battle)

            assert result == joined_orders


def test_get_orders_returns_tera_orders_when_available(
    metronome_player: MetronomePlayer,
    default_double_battle: DoubleBattle,
):
    tera_double_battle_order = create_double_battle_order_with_first(
        create_tera_order()
    )
    default_double_battle_order = create_default_double_battle_order()

    joined_orders = [tera_double_battle_order, default_double_battle_order]

    with patch.object(DoubleBattleOrder, "join_orders") as join_orders_mock:
        with patch.object(
            metronome_player._tera_strategy,
            "filter_orders",
        ) as filter_orders_mock:
            join_orders_mock.return_value = joined_orders
            filter_orders_mock.return_value = [tera_double_battle_order]

            result = metronome_player._get_orders(default_double_battle)

            assert result == [tera_double_battle_order]


async def test_choose_move_raises_error_for_non_double_battle(
    metronome_player: MetronomePlayer,
):
    battle = Mock(spec=AbstractBattle)

    with pytest.raises(TypeError):
        await metronome_player.choose_move(battle)


async def test_choose_move_returns_random_order(
    default_double_battle: DoubleBattle,
    metronome_player: MetronomePlayer,
):
    order_1 = DoubleBattleOrderBuilder().build()
    order_2 = DoubleBattleOrderBuilder().build()

    with patch.object(metronome_player, "_get_orders") as player_mock:
        with patch("random.choice") as choice_mock:
            player_mock.return_value = [order_1, order_2]
            choice_mock.return_value = order_2

            result = await metronome_player.choose_move(default_double_battle)

            assert result == order_2


async def test_choose_move_fallback_when_no_orders(
    default_double_battle: DoubleBattle,
    empty_double_battle: DoubleBattle,
    metronome_player: MetronomePlayer,
):
    with patch.object(metronome_player, "_get_orders") as mock:
        mock.return_value = empty_double_battle

        result = await metronome_player.choose_move(default_double_battle)

        assert isinstance(result, DoubleBattleOrder)
        assert isinstance(result.first_order, DefaultBattleOrder)
        assert isinstance(result.second_order, DefaultBattleOrder)


async def test_choose_move_handles_exception(
    default_double_battle: DoubleBattle,
    metronome_player: MetronomePlayer,
):
    with patch.object(metronome_player, "_get_orders") as mock:
        mock.side_effect = Exception("test_error")

        result = await metronome_player.choose_move(default_double_battle)

        assert isinstance(result, DoubleBattleOrder)
        assert isinstance(result.first_order, DefaultBattleOrder)
        assert isinstance(result.second_order, DefaultBattleOrder)
