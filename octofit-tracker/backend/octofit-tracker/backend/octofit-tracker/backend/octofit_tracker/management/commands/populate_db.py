
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):


        # Drop collections directly using PyMongo
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        db['leaderboard'].drop()
        db['activities'].drop()
        db['workouts'].drop()
        db['users'].drop()
        db['teams'].drop()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create workouts
        pushups = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Run 5km', difficulty='Medium')

        # Create activities
        Activity.objects.create(user=tony, type='Pushups', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Running', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Pushups', duration=25, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Running', duration=50, date=timezone.now().date())

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=98)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
