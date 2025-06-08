async function addSong() {
  const title = document.getElementById('title').value;
  const artist = document.getElementById('artist').value;
  const duration = document.getElementById('duration').value;
  const youtube_url = document.getElementById('youtube_url').value;

  await fetch('/add', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, artist, duration, youtube_url })
  });

  loadSongs();
}

async function loadSongs() {
  const res = await fetch('/songs');
  const songs = await res.json();
  const list = document.getElementById('playlist');
  list.innerHTML = '';
  songs.forEach(song => {
    const li = document.createElement('li');
    li.innerHTML = `
      <strong>${song.title}</strong> by ${song.artist} (${song.duration})
      ${song.youtube_url ? `<br><iframe width="300" height="170" src="${convertToEmbed(song.youtube_url)}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>` : ''}
    `;
    list.appendChild(li);
  });
}

function convertToEmbed(url) {
  const videoId = url.split("v=")[1]?.split("&")[0];
  return `https://www.youtube.com/embed/${videoId}`;
}

async function downloadCSV() {
  window.location.href = '/download';
}

loadSongs();
