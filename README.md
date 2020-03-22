# JdeRobot-PythonChallenge-GSOC2020

The Python Challenge is basically coding Conway's Game of Life in Python.

## `cgol.py`
This is the Python Module I coded as a solution. There all functions needed to launch the game in a application script are found. Have in mind I used `matplotlib` only for illustration purposes. I know it is not a built-in library. However, didn't like the way I could show the array grid in the terminal only using prints, really hope this doesn't affect in my application. Basically `matplotlib` is only responsible for showing the grid.

### Sample application
Here you can also find a file called `app.py` and `config.json`. I used this both to test the solution. `app.py` basically is responsible for using the functions found in `cgol.py` and launch the game.

Also it is important to know the structure of the `config.json` file. There you can configure the grid size and interval in which the grid changes. If another configuration file is desired to be used, that should be changed in the `loadConfig` function in `app.py`.

```json
{
	"gridsize": 100,
	"interval": 300
}
```

To run the sample application just run:

`python3 app.py`

This will run the game to times using different config files.

