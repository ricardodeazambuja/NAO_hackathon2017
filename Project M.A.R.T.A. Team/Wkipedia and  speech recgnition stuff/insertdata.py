from naoqi import ALProxy

try:
  # create proxy on ALMemory
  memProxy = ALProxy("ALMemory","crackle.local",9559)

  #insertData. Value can be int, float, list, string
  memProxy.insertData("myValueName1", "myValue1")

  #getData
  print "The value of myValueName1 is", memProxy.getData("myValueName1")

  memProxy.raiseEvent("My event", "data iss there")
except RuntimeError,e:
  # catch exception
  print "error insert data", e
