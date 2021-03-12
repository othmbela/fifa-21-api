from rest_framework import status, test

from .models import Player



class PlayerCreateTestCase(test.APITestCase):

    def test_create_player(self):
        """
        Ensure we can create a new player object.
        """

        initial_player_count = Player.objects.count()
        player_attrs = {
            "short_name": "O. Belarbi",
            "full_name": "Othmane Belarbi",
            "country": "France",
            "age": 20,
            "overall_rating":99,
            "potential": 99,
            "club": "Lille OSC",
            "height": 180,
            "weight": 80,
            "foot": "Left",
            "best_postion": "CM",
            "value": 103500000,
            "wage": 560000,
            "VIT": 99,
            "TIR": 99,
            "PAS": 99,
            "DRI": 99,
            "DEF": 99,
            "PHY": 99,
            "country_code": "FR"
        }

        response = self.client.post('/api/v1/player/add', player_attrs)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Player.objects.count(), initial_player_count + 1)
        for attr, expected_value in player_attrs.items():
            self.assertEqual(expected_value, response.data[attr])


class PlayerUpdateTestCase(test.APITestCase):

    def setUp(self):
        Player.objects.create(
            short_name="O. Belarbi",
            full_name="Othmane Belarbi",
            country="France",
            age=20,
            overall_rating=9,
            potential=99,
            club="Lille OSC",
            height=180,
            weight=80,
            foot="Left",
            best_postion="CM",
            value=103500000,
            wage=560000,
            VIT=99,
            TIR=99,
            PAS=99,
            DRI=99,
            DEF=99,
            PHY=99,
            country_code="FR"
        )

    def test_update_put_player(self):
        """
        Ensure we can update a player object.
        """

        player_attrs = {
            "short_name": "O. Belarbi",
            "full_name": "Othmane Belarbi",
            "country": "France",
            "age": 20,
            "overall_rating":0,
            "potential": 0,
            "club": "Lille OSC",
            "height": 180,
            "weight": 80,
            "foot": "Left",
            "best_postion": "CM",
            "value": 103500000,
            "wage": 560000,
            "VIT": 0,
            "TIR": 0,
            "PAS": 0,
            "DRI": 0,
            "DEF": 0,
            "PHY": 0,
            "country_code": "FR"
        }

        response = self.client.put('/api/v1/player/3/update', player_attrs)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for attr, expected_value in player_attrs.items():
            self.assertEqual(expected_value, response.data[attr])


class PlayerDeleteTestCase(test.APITestCase):

    def setUp(self):
        Player.objects.create(
            short_name="O. Belarbi",
            full_name="Othmane Belarbi",
            country="France",
            age=20,
            overall_rating=9,
            potential=99,
            club="Lille OSC",
            height=180,
            weight=80,
            foot="Left",
            best_postion="CM",
            value=103500000,
            wage=560000,
            VIT=99,
            TIR=99,
            PAS=99,
            DRI=99,
            DEF=99,
            PHY=99,
            country_code="FR"
        )

    def test_delete_player(self):
        """
        Ensure we can delete a player object.
        """

        initial_player_count = Player.objects.count()

        response = self.client.delete('/api/v1/player/2/delete')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Player.objects.count(), initial_player_count - 1)

