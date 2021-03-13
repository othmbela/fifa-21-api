from rest_framework import status, test

from .models import Team



class TeamCreateTestCase(test.APITestCase):

    def test_create_team(self):
        """
        Ensure we can create a new team object.
        """

        initial_team_count = Team.objects.count()
        team_attrs = {
            "name": "FC Othmane",
            "country": "France",
            "league": "Ligue 1",
            "overall": 0,
            "attack": 0,
            "midfield": 0,
            "defence": 0,
            "transfer_budget": 0,
            "players": 0,
            "hits": 0
            }

        response = self.client.post('/api/v1/team/add', team_attrs)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), initial_team_count + 1)
        for attr, expected_value in team_attrs.items():
            self.assertEqual(expected_value, response.data[attr])


class TeamUpdateTestCase(test.APITestCase):

    def setUp(self):
        Team.objects.create(
            name="FC Othmane",
            country="France",
            league="Ligue 1",
            overall=0,
            attack=0,
            midfield=0,
            defence=0,
            transfer_budget=0,
            players=0,
            hits=0
        )

    def test_update_put_team(self):
        """
        Ensure we can update a Team object.
        """

        team_attrs = {
            "name": "FC Othmane",
            "country": "France",
            "league": "Ligue 1",
            "overall": 0,
            "attack": 0,
            "midfield": 0,
            "defence": 0,
            "transfer_budget": 0,
            "players": 0,
            "hits": 0
            }

        response = self.client.put('/api/v1/team/6/update', team_attrs)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for attr, expected_value in team_attrs.items():
            self.assertEqual(expected_value, response.data[attr])


class TeamDeleteTestCase(test.APITestCase):

    def setUp(self):
        Team.objects.create(
            name="FC Othmane",
            country="France",
            league="Ligue 1",
            overall=0,
            attack=0,
            midfield=0,
            defence=0,
            transfer_budget=0,
            players=0,
            hits=0
        )

    def test_delete_team(self):
        """
        Ensure we can delete a Team object.
        """

        initial_team_count = Team.objects.count()

        response = self.client.delete('/api/v1/team/5/delete')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Team.objects.count(), initial_team_count - 1)

