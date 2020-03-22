import cgol


(N, updateInterval)=cgol.loadConfig('smallconfig.json')
grid=cgol.gridInit(N)
cgol.gameLaunch(grid, N, updateInterval)

(N, updateInterval)=cgol.loadConfig('bigconfig.json')
grid=cgol.gridInit(N)
cgol.gameLaunch(grid, N, updateInterval)

