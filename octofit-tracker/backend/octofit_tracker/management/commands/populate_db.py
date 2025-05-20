from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='password1')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='password2')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='password3')

        # Teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)
        team2 = Team.objects.create(name='Team Beta')
        team2.members.add(user3)

        # Workouts
        workout1 = Workout.objects.create(name='5K Run', description='Run 5 kilometers', suggested_points=50)
        workout2 = Workout.objects.create(name='Pushups', description='Do 50 pushups', suggested_points=30)

        # Activities
        Activity.objects.create(user=user1, activity_type='run', duration=30, date='2025-05-01', points=50)
        Activity.objects.create(user=user2, activity_type='pushups', duration=10, date='2025-05-02', points=30)
        Activity.objects.create(user=user3, activity_type='walk', duration=60, date='2025-05-03', points=20)

        # Leaderboard
        Leaderboard.objects.create(user=user1, total_points=50)
        Leaderboard.objects.create(user=user2, total_points=30)
        Leaderboard.objects.create(user=user3, total_points=20)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
