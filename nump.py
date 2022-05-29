import numpy as np
# # #
# # # a = np.array([1, 2, 3])
# # # print(a)
# # #
# # # b = np.arange (1, 4, 1, dtype = 'float64')
# # # print(type(b))
# # # print(b.dtype)
# # # print(b.shape)
# # #
# # # c = np.array([[0,1],[0, 1]])
# # # print(c)
# # # print(c.shape)
# # # print(c.ndim)
# # import numpy as np
# #
# # zera = np.zeros((5, 5))
# # print(zera)
# # jedynki = np.ones((5, 5))
# # print(jedynki)
# #
# # pusta = np.empty((2, 2))
# # print(pusta)
# # pusta[1][1] = 2
# # print(pusta)
# #
# # a = np.arange(1, 5, 0.5)
# # print(a)
# #
# # b = np.linspace(1, 2, 5, endpoint=False)
# # print(b)
# #
# # c, d = np.indices((5, 5))
# # print(c)
# # print(d)
# #
# # e, f = np.mgrid[0:3, 0:3]
# # print(e)
# # print(f)
# #
# # g = np.diag([x for x in range(5)], k = -1)
# # print(g)
# # h = np.fromiter(range(5), dtype='int32')
# # print(h)
# import numpy as np
#
# marcin ='Marcin'
# # mar = np.frombuffer(marcin, dtype='S1') #s1-długość tego el,  b -popszedza każdy el.
# # print(mar)
#
# mar_1 = np.array(list(marcin))
# print(mar_1)
#
# mar_2 = np.array(list(b'Marcin'))
# print(mar_2)
# mar_3 = np.fromiter(marcin, dtype='S1')
# mar_4 = np.fromiter(marcin, dtype='U1')
# print(mar_3)
# print(mar_4)

#
# a = np.ones((2, 2))
# b = np.ones((2, 2))
# c = a + b
# print(c)



# a = np.arange(10)
# print(a)
#
# s = slice(2, 7, 2)
# print(a[s])
# s = range(2, 7, 2)
# print(a[s])
# print(a[2:7:2])
# print(a[1:])
# print(a[2:5])




# a = np.arange(25)
# mat = a.reshape((5, 5))
# print(mat)
# # print(mat[1:2])
# # print(mat[:,1:2])
# print(mat[2:5, 1:3])

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 6]])
print(x)

rows = np.array([[0, 0],[3, 3]])
cols = np.array([[0, 2],[0, 2]])

y = x[rows, cols]
print(y)