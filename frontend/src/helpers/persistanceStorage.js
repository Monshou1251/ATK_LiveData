export const getItem = (key) => {
  // key это имя по которому мы получим что-то из localStorage
  try {
    return JSON.parse(localStorage.getItem(key))
    // если мы что-то получаем из localStorage это всегда строка
  } catch (e) {
    console.log('Error getting data from localStorage', e)
    return null
  }
}

export const setItem = (key, data) => {
  // key - куда мы записываем, data - что мы записываем
  try {
    localStorage.setItem(key, JSON.stringify(data))
  } catch (e) {
    console.log('Error saving data from localStorage', e)
  }
}
