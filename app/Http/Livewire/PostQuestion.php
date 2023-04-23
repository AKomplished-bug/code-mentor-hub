<?php

namespace App\Http\Livewire;

use Livewire\Component;

class PostQuestion extends Component
{

    public $question;

    public function render()
    {
        return view('livewire.post-question');
    }
}