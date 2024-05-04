<x-app-layout>
    <x-slot name="header">
        <h2 class="font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight">
            {{ __('Assignment') }}
        </h2>
    </x-slot>

    <div class="py-12">
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
            <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-xl sm:rounded-lg">
                <!-- Your assignment content goes here -->
                <!-- For example, you can add a form to submit assignments -->
                <form action="{{ route('assignment') }}" method="POST">
                    @csrf
                    <div class="mb-4">
                        <label for="assignment_file" class="block text-gray-700 text-sm font-bold mb-2">Assignment File:</label>
                        <input type="file" name="assignment_file" id="assignment_file" class="border-gray-300 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md">
                    </div>
                    <div class="mb-4">
                        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Submit Assignment</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</x-app-layout>
