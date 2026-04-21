from django.shortcuts import render, get_object_or_404, redirect
from .models import Workout
from .forms import WorkoutForm

def workout_list(request):
    workouts = Workout.objects.all().order_by('-created_at')
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'workouts/workout_form.html', {'form': form})

def workout_detail(request, pk):
    workouts =get_object_or_404(Workout, pk=pk)
    return render(request, 'workouts/workout_detail.html', {'workouts': workouts})

def workout_done(request, pk):
    if request.method == 'POST':
        workout = get_object_or_404(Workout, pk=pk)
        workout = get_object_or_404(Workout, pk=pk)
        workout.is_done = True
        workout.save()
    return redirect('workout_list')

def workout_delete(request, pk):
    if request.method == 'POST':
        workout = get_object_or_404(Workout, pk=pk)
        workout.delete()
    return redirect('workout_list')

def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workouts/workout_form.html', {'form': form})