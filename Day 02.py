class RemoveElement
  def removeElements(num : list[int], val: int)-> int:
    k=0
    for i in range(len(nums)):
      if num[i]!=val:
        num[k]=num[i]
        k+=1
    return k
